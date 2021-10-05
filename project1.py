"""
UMass ECE 241 - Advanced Programming
Project #1   Fall 2021
project1.py - Sorting and Searching

"""

import matplotlib.pyplot as plt


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
        return 'name: ' + self.sname + '; ' + 'symbol: ' + self.symbol + '; ' + 'val: ' + str(self.val) + '; ' + \
               'price: ' + str(self.prices[len(self.prices)-1])



"""
StockLibrary class to mange stock objects
"""
class StockLibrary:

    """
    Constructor to initialize the StockLibrary
    """
    def __init__(self, stockList: list):
        self.stockList = stockList
        self.size = len(self.stockList)
        self.isSorted = False



    """
    The loadData method takes the file name of the input dataset,
    and stores the data of stocks into the library. 
    Make sure the order of the stocks is the same as the one in the input file. 
    """
    def loadData(self, filename: str):
        file = open(filename, 'r')
        stocks = []
        infoList = file.readlines()[1:]
        tempList = []
        for i in infoList:
            tempList = i.split('|')
            stocks.append(Stock(tempList[0], tempList[1], tempList[2], tempList[3:22]))

        print(stocks[0])
        self.stockList = stocks;



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
                    return 'name: ' + i.sname + '; ' + 'symbol: ' + i.symbol + '; ' + 'val: ' + str(i.val) + '; ' + \
            'price: ' + str(i.prices[len(i.prices)-1])
        if attribute == 'symbol':
            for i in self.stockList:
                if i.symbol == query:
                    return 'name: ' + i.sname + '; ' + 'symbol: ' + i.symbol + '; ' + 'val: ' + str(i.val) + '; ' + \
            'price: ' + str(i.prices[len(i.prices)-1])
        return 'Stock not found'



    """
    Sort the stockList using QuickSort algorithm based on the stock symbol.
    The sorted array should be stored in the same stockList.
    Remember to change the isSorted variable after sorted
    """
    def quickSort(self):

        first = 0;
        last = len(self.stockList)-1
        lowerSplitPoint = 0
        upperSplitPoint = 0

        if first < last:
            pivotvalue = self.stockList[first].symbol
            leftmark = first +1
            rightmark = last
            done = False
            while not done:
                while leftmark <= rightmark and self.stockList[leftmark].symbol <= pivotvalue:
                    leftmark = leftmark + 1

                while rightmark >= leftmark and self.stockList[rightmark].symbol >= pivotvalue:
                    rightmark = rightmark - 1

                if rightmark < leftmark:
                    done = True
                else:
                    tempValue = self.stockList[leftmark]
                    self.stockList[leftmark] = self.stockList[rightmark]
                    self.stockList[rightmark] = tempValue

            tempValue = self.stockList[first]
            self.stockList[first] = self.stockList[rightmark]
            self.stockList[rightmark] = tempValue
            upperSplitPoint = rightmark + 1
            lowerSplitPoint = leftmark - 1

        while upperSplitPoint < last:
            pivotvalue = self.stockList[first].symbol
            leftmark = upperSplitPoint + 1
            rightmark = last
            done = False
            while not done:
                while leftmark <= rightmark and self.stockList[leftmark].symbol <= pivotvalue:
                    leftmark = leftmark + 1

                while rightmark >= leftmark and self.stockList[rightmark].symbol >= pivotvalue:
                    rightmark = rightmark - 1

                if rightmark < leftmark:
                    done = True
                else:
                    tempValue = self.stockList[leftmark]
                    self.stockList[leftmark] = self.stockList[rightmark]
                    self.stockList[rightmark] = tempValue

            tempValue = self.stockList[upperSplitPoint]
            self.stockList[upperSplitPoint] = self.stockList[rightmark]
            self.stockList[rightmark] = tempValue
            upperSplitPoint = rightmark + 1

        while lowerSplitPoint > first:
            pivotvalue = self.stockList[first].symbol
            leftmark = first+1
            rightmark = lowerSplitPoint
            done = False
            while not done:
                while leftmark <= rightmark and self.stockList[leftmark].symbol <= pivotvalue:
                    leftmark = leftmark + 1

                while rightmark >= leftmark and self.stockList[rightmark].symbol >= pivotvalue:
                    rightmark = rightmark - 1

                if rightmark < leftmark:
                    done = True
                else:
                    tempValue = self.stockList[leftmark]
                    self.stockList[leftmark] = self.stockList[rightmark]
                    self.stockList[rightmark] = tempValue

            tempValue = self.stockList[upperSplitPoint]
            self.stockList[upperSplitPoint] = self.stockList[rightmark]
            self.stockList[rightmark] = tempValue
            lowerSplitPoint = rightmark - 1

        self.isSorted=True



    """
    build a balanced BST of the stocks based on the symbol. 
    Store the root of the BST as attribute bst, which is a TreeNode type.
    """
    def buildBST(self):

        pass

    """
    Search a stock based on the symbol attribute. 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """
    def searchBST(self, query, current='dnode'):

        pass



# WRITE YOUR OWN TEST UNDER THIS IF YOU NEED
if __name__ == '__main__':

    testStock = Stock('Exxon Mobil Corporation', 'XOM', 384845.80,[41.50, 43.50, 44.61, 44.96, 45.46, 46.84, 47.8])
    stockLib = StockLibrary([])
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

