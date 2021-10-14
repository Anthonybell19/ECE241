"""
UMass ECE 241 - Advanced Programming
Project #1   Fall 2021
project1.py - Sorting and Searching

"""
import time


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


    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
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
        if node.parent:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        if rotRoot is None:
            return False
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
        if rotRoot is None:  # null error checking
            return False
        newRoot = rotRoot.leftChild  # create new root obj
        rotRoot.leftChild = newRoot.rightChild  # move old root's left child
        if newRoot.rightChild:
            newRoot.rightChild.parent = rotRoot  # set the new root's right child's parent to be old root
        newRoot.parent = rotRoot.parent  # replace old root parent with new root parent
        if rotRoot is self.root:
            self.root = newRoot  # set new root to be root obj if it's replacing the root obj
        else:
            if rotRoot.parent.rightChild is rotRoot:
                rotRoot.parent.rightChild = newRoot  # set the old root's parent children
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot  # setting new root right child to be old root
        rotRoot.parent = newRoot  # setting old root's parent to be new root
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)  # setting both roots balance
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)  # factor

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)




class Stock:


    def __init__(self, sname: str, symbol: str, val: float, prices: list):
        # constructing stock obj
        self.sname = sname
        self.symbol = symbol
        self.val = val
        self.prices = prices



    def __str__(self):
        # string function for printing out stock information
        return 'name: ' + self.sname + '; ' + 'symbol: ' + self.symbol + '; ' + 'val: ' + str(
            round(float(self.val), 1)) + '; ' + \
               'price:' + str(self.prices[len(self.prices) - 1])


class StockLibrary:

    def __init__(self):
        # constructor for stock library obj
        self.stockList = []
        self.size = len(self.stockList)
        self.isSorted = False
        self.bst = None

    def loadData(self, filename: str):
        file = open(filename, 'r')
        stocks = []
        infoList = file.readlines()[1:]  # grab everything after the first line of data
        for i in infoList:
            tempList = i.split('|')  # break list a part based on | operator
            stocks.append(Stock(tempList[0], tempList[1], tempList[2], tempList[3:22]))  # append a new stock object to
            # a list based off of stock information provided

        self.stockList = stocks  # set class variables
        self.size = len(self.stockList)

    def linearSearch(self, query: str, attribute: str):
        linearStart = time.time()
        if attribute == 'name':  # see if searching by stock name
            for i in self.stockList:
                if i.sname == query:  # iterate through list of stocks by name and return information if found
                    linearEnd = time.time()
                    print(linearEnd - linearStart)
                    return 'name: ' + i.sname + '; ' + 'symbol: ' + i.symbol + '; ' + 'val: ' + str(
                        round(float(i.val), 1)) + '; ' + \
                           'price:' + str(i.prices[len(i.prices) - 1])
        if attribute == 'symbol':  # see if searching by stock symbol
            for i in self.stockList:
                if i.symbol == query:  # iterate through list of stocks by symbol and return information if found
                    
                    return 'name: ' + i.sname + '; ' + 'symbol: ' + i.symbol + '; ' + 'val: ' + str(
                        round(float(i.val), 1)) + '; ' + \
                           'price:' + str(i.prices[len(i.prices) - 1])
        return 'Stock not found'

    def quickSort(self):
        # calls helper function and sets class variable isSorted to be true
        self.quickSortHelper(self.stockList, 0, len(self.stockList) - 1)
        self.isSorted = True

    def quickSortHelper(self, list, first, last):
        # manages split point value and recursion for the quicksort function
        if first < last:
            splitpoint = self.partition(list, first, last)
            self.quickSortHelper(list, first, splitpoint - 1)
            self.quickSortHelper(list, splitpoint + 1, last)

    def partition(self, list, first, last):
        pivotvalue = list[first].symbol  # value to be inserted in the sort
        leftmark = first + 1  # lower marker
        rightmark = last  # upper marker
        done = False
        while not done:
            while leftmark <= rightmark and list[leftmark].symbol <= pivotvalue:  # find a value on lower half greater
                # than pivot value
                leftmark = leftmark + 1

            while rightmark >= leftmark and list[
                rightmark].symbol >= pivotvalue:  # find a value on upper half less than
                # pivot value
                rightmark = rightmark - 1

            if rightmark < leftmark:  # if marks cross, stop
                done = True
            else:  # swap left and right mark values if LM value > PV and RM value < PV
                temp = list[leftmark]
                list[leftmark] = list[rightmark]
                list[rightmark] = temp

        temp = list[first]
        list[first] = list[rightmark]  # swap pivot value and right mark value
        list[rightmark] = temp

        return rightmark

    def buildBST(self):
        bstStart = time.time()
        tree = AvlTree()  # construct AVL tree
        for i in self.stockList:
            if i is not None:
                tree.put(i.symbol, i.val)  # add to the binary tree, sort by the stock symbol

        self.bst = tree.root  # self the bst class variable to be the root of the tree
        bstEnd = time.time()

    def searchBST(self, query, current='dnode'):
        stock = Stock('', '', 0, [])  # create a stock to be passed into find function later
        for i in self.stockList:
            if i.symbol == query:
                stock = i  # find corresponding stock obj
        if self.bst:
            return self.bst.find(query, stock)  # search binary tree for obj, use stock obj for returning info
        else:
            return 'stock not found'

        pass


# WRITE YOUR OWN TEST UNDER THIS IF YOU NEED
if __name__ == '__main__':
    testStock = Stock('Exxon Mobil Corporation', 'XOM', 384845.80, [41.50, 43.50, 44.61, 44.96, 45.46, 46.84, 47.8])
    stockLib = StockLibrary()
    testSymbol = 'GOOG'
    testName = 'General Electric Company'
    print("\n-------load dataset-------")
    stockLib.loadData("stock_database.csv")


    print("\n-------linear search-------")

    print(stockLib.linearSearch(testSymbol, "symbol"))


    # print(stockLib.linearSearch(testSymbol, "symbol"))
    # print(stockLib.linearSearch(testName, "name"))

    print("\n-------quick sort-------")
    print(stockLib.isSorted)
    stockLib.quickSort()
    print(stockLib.isSorted)

    print("\n-------build BST-------")
    bstStart = time.time()
    stockLib.buildBST()
    bstEnd = time.time()
    print(bstEnd - bstStart)
    print("\n---------search BST---------")
    print(stockLib.searchBST(testSymbol))
