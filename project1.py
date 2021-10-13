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
        self.balanceFactor = 0

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

    def find(self, key, stock):
        if self.key == key:
            return 'name: ' + stock.sname + '; ' + 'symbol: ' + stock.symbol + '; ' + 'val: ' + str(
                round(float(stock.val), 1)) + '; ' + \
                   'price:' + str(stock.prices[len(stock.prices) - 1])
        elif key < self.key:
            if self.hasLeftChild():
                return self.leftChild.find(key, stock)
            else:
                return 'stock not found'
        else:
            if self.hasRightChild():
                return self.rightChild.find(key, stock)
            else:
                return 'stock not found'


class BinarySearchTree:

    def __init__(self):
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


class AvlTree(BinarySearchTree):
    '''An extension t the BinarySearchTree data structure which
    strives to keep itself balanced '''

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChile)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balancefactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild is not None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild is not None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftchilc)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


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
            round(float(self.val), 1)) + '; ' + \
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
                        round(float(i.val), 1)) + '; ' + \
                           'price:' + str(i.prices[len(i.prices) - 1])
        if attribute == 'symbol':
            for i in self.stockList:
                if i.symbol == query:
                    return 'name: ' + i.sname + '; ' + 'symbol: ' + i.symbol + '; ' + 'val: ' + str(
                        round(float(i.val), 1)) + '; ' + \
                           'price:' + str(i.prices[len(i.prices) - 1])
        return 'Stock not found'

    """
    Sort the stockList using QuickSort algorithm based on the stock symbol.
    The sorted array should be stored in the same stockList.
    Remember to change the isSorted variable after sorted
    """

    def quickSort(self):
        self.quickSortHelper(self.stockList, 0, len(self.stockList) - 1)
        self.isSorted = True

    def quickSortHelper(self, list, first, last):
        if first < last:
            splitpoint = self.partition(list, first, last)
            self.quickSortHelper(list, first, splitpoint - 1)
            self.quickSortHelper(list, splitpoint + 1, last)

    def partition(self, list, first, last):
        pivotvalue = list[first].symbol
        leftmark = first + 1
        rightmark = last
        done = False
        while not done:
            while leftmark <= rightmark and list[leftmark].symbol <= pivotvalue:
                leftmark = leftmark + 1

            while rightmark >= leftmark and list[rightmark].symbol >= pivotvalue:
                rightmark = rightmark - 1

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
        node = TreeNode('', '')
        tree = AvlTree()
        for i in self.stockList:
            node = TreeNode(i.symbol, i.val)
            tree.put(i.symbol, i.val)
            tree.rebalance(node)
        self.bst = tree.root

    """
    Search a stock based on the symbol attribute. 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """

    def searchBST(self, query, current='dnode'):
        stock = Stock('', '', 0, [])
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
