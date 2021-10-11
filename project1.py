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


class BinarySearchTree:

    def __init__(self, stockList: list):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


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
               'price: ' + str(self.prices[len(self.prices) - 1])


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

        first = 0;
        last = len(self.stockList) - 1
        lowerSplitPoint = 0
        upperSplitPoint = 0

        if first < last:
            pivotvalue = self.stockList[first].symbol
            leftmark = first + 1
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
            leftmark = first + 1
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

        self.isSorted = True

    """
    build a balanced BST of the stocks based on the symbol. 
    Store the root of the BST as attribute bst, which is a TreeNode type.
    """

    def buildBST(self):
        self._put(0, len(self.stockList))

    def _put(self, start, end):
        if start < end:
            mid = (start + end) // 2
            node = TreeNode(mid, self.stockList[mid])
            node.leftChild = self._put(start, mid - 1)
            node.rightChild = self._put(mid + 1, end)
            if start == 0 and end == len(self.stockList):
                self.bst = node
            return node

    """
    Search a stock based on the symbol attribute. 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """

    # work
    def _find(self, key, currentNode):
        if currentNode is not None:
            if key == currentNode.payload.symbol:
                return 'FOUND NODE'
            if key < currentNode.payload.symbol:
                if currentNode.hasLeftChild:
                    return self._find(key, currentNode.leftChild)
            elif currentNode.hasRightChild:
                return self._find(key, currentNode.rightChild)
        else:
            return 'not found'

    def searchBST(self, query, current='dnode'):
        if self.bst:
            return self._find(query, self.bst)
        else:
            return 'Stock not found'

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
