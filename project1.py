"""
UMass ECE 241 - Advanced Programming
Project #1   Fall 2021
project1.py - Sorting and Searching

"""

import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def insert(self, key, data):
        if self.key == key:
            return False
        elif key < self.key:
            if self.hasLeftChild():
                return self.leftChild.insert(key,data)
            else:
                self.leftChild = TreeNode(key, data)
                return True
        else:
            if self.hasRightChild():
                return self.rightChild.insert(key,data)
            else:
                self.rightChild = TreeNode(key, data)
                return True

    def find(self, key, stock):
        if self.key == key:
            return 'name: ' + stock.sname + '; ' + 'symbol: ' + stock.symbol + '; ' + 'val: ' + str(
                        round(float(stock.val),1)) + '; ' + \
                           'price:' + str(stock.prices[len(stock.prices) - 1])
        elif key < self.key:
            if self.hasLeftChild():
                return self.leftChild.find(key)
            else:
                return 'stock not found'
        else:
            if self.hasRightChild():
                return self.rightChild.find(key)
            else:
                return 'stock not found'



"""
Stock class for stock objects
"""


class Stock:
    """
    Constructor to initialize the stock object
    """

    def __init__(self, sname: str, symbol: str, val: float, prices: list):
        self.sname = sname
        self.symbol = symbol
        self.val = val
        self.prices = prices

    """
    return the stock information as a string, including name, symbol, 
    market value, and the price on the last day (2021-02-01). 
    For example, the string of the first stock should be returned as: 
    “name: Exxon Mobil Corporation; symbol: XOM; val: 384845.80; price:44.84”. 
    """

    def __str__(self):
        return 'name: ' + self.sname + '; ' + 'symbol: ' + self.symbol + '; ' + 'val: ' + str(
                        round(float(self.val),1)) + '; ' + \
               'price:' + str(self.prices[len(self.prices) - 1])


"""
StockLibrary class to mange stock objects
"""


class StockLibrary:
    """
    Constructor to initialize the StockLibrary
    """

    def __init__(self):
        self.stockList = []
        self.size = len(self.stockList)
        self.isSorted = False
        self.bst = None
    """
    The loadData method takes the file name of the input dataset,
    and stores the data of stocks into the library. 
    Make sure the order of the stocks is the same as the one in the input file. 
    """

    def loadData(self, filename: str):
        file = open(filename, 'r')
        stocks = []
        infoList = file.readlines()[1:]
        for i in infoList:
            tempList = i.split('|')
            stocks.append(Stock(tempList[0], tempList[1], tempList[2], tempList[3:22]))

        self.stockList = stocks;
        self.size = len(self.stockList)

    """
    The linearSearch method searches the stocks based on sname or symbol.
    It takes two arguments as the string for search and an attribute field 
    that we want to search (“name” or “symbol”). 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """

    def linearSearch(self, query: str, attribute: str):

        if attribute == 'name':
            for i in self.stockList:
                if i.sname == query:
                    return 'name: ' + i.sname + '; ' + 'symbol: ' + i.symbol + '; ' + 'val: ' + str(
                        round(float(i.val),1)) + '; ' + \
                           'price:' + str(i.prices[len(i.prices) - 1])
        if attribute == 'symbol':
            for i in self.stockList:
                if i.symbol == query:
                    return 'name: ' + i.sname + '; ' + 'symbol: ' + i.symbol + '; ' + 'val: ' + str(
                        round(float(i.val),1)) + '; ' + \
                           'price:' + str(i.prices[len(i.prices) - 1])
        return 'Stock not found'

    """
    Sort the stockList using QuickSort algorithm based on the stock symbol.
    The sorted array should be stored in the same stockList.
    Remember to change the isSorted variable after sorted
    """
    def quickSort(self):
        self.quickSortHelper(self.stockList, 0, len(self.stockList)-1)
        self.isSorted = True

    def quickSortHelper(self, list, first, last):
        if first < last:
            splitpoint = self.partition(list, first, last)
            self.quickSortHelper(list, first, splitpoint - 1)
            self.quickSortHelper(list, splitpoint + 1, last)

    def partition(self, list, first, last):
        pivotvalue = list[first].symbol
        leftmark = first+1
        rightmark = last
        done = False
        while not done:
            while leftmark <= rightmark and list[leftmark].symbol <= pivotvalue:
                leftmark = leftmark + 1

            while rightmark >= leftmark and list[rightmark].symbol >= pivotvalue:
                rightmark = rightmark -1

            if rightmark < leftmark:
                done = True
            else:
                temp = list[leftmark]
                list[leftmark] = list[rightmark]
                list[rightmark] = temp

        temp = list[first]
        list[first] = list[rightmark]
        list[rightmark] = temp


        return rightmark

    """
    build a balanced BST of the stocks based on the symbol. 
    Store the root of the BST as attribute bst, which is a TreeNode type.
    """

    def buildBST(self):
        for i in self.stockList:
            if i == self.stockList[0]:
                self.bst = TreeNode(i.symbol, i.val)
            if self.bst:
                self.bst.insert(i.symbol, i.val)



    """
    Search a stock based on the symbol attribute. 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """



    def searchBST(self, query, current='dnode'):
        for i in self.stockList:
            if i.symbol == query:
                stock = i
        if self.bst:
            return self.bst.find(query, stock)
        else:
            return 'stock not found'

        pass


# WRITE YOUR OWN TEST UNDER THIS IF YOU NEED
if __name__ == '__main__':
    testStock = Stock('Exxon Mobil Corporation', 'XOM', 384845.80, [41.50, 43.50, 44.61, 44.96, 45.46, 46.84, 47.8])
    stockLib = StockLibrary()
    testSymbol = 'GE'
    testName = 'General Electric Company'
    print("\n-------load dataset-------")
    stockLib.loadData("stock_database.csv")

    print("\n-------linear search-------")
    print(stockLib.linearSearch(testSymbol, "symbol"))
    print(stockLib.linearSearch(testName, "name"))

    print("\n-------quick sort-------")
    print(stockLib.isSorted)
    stockLib.quickSort()
    print(stockLib.isSorted)

    print("\n-------build BST-------")
    stockLib.buildBST()

    print("\n---------search BST---------")
    print(stockLib.searchBST(testSymbol))