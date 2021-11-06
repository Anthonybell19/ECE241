
from Graph import *
import random


class ISPNetwork:

    def __init__(self):
        self.network = Graph()
        self.MST = Graph()

    def buildGraph(self, filename):
        graph = Graph()
        file = open(filename, 'r')
        info = file.readlines()
        for i in info:
            l = i.split(',')
            w = l[2].split('\n')
            weight = float(w[0])
            graph.addEdge(l[0], l[1], weight)
        self.network = graph

    def pathExist(self, router1, route2):
        r1 = self.network.getVertex(router1)
        b = self.testPath(r1, route2)
        self.resetNetwork()
        return b

    def resetNetwork(self):
        if self.network is not None:
            for i in self.network:
                i.setColor('white')

    def resetMST(self):
        if self.MST is not None:
            for i in self.MST:
                i.setColor('white')

    def testPath(self, start, checkId):
        vertQueue = Queue()
        vertQueue.enqueue(start)
        while vertQueue.size() > 0:
            currentVert = vertQueue.dequeue()
            if currentVert is not None:
                for nbr in currentVert.getConnections():
                    if nbr.getColor() == 'white':
                        if nbr.getId() == checkId:
                            return True
                        nbr.setColor('gray')
                        vertQueue.enqueue(nbr)
                currentVert.setColor('black')
        return False


    def buildMST(self):
        tempGraph = self.network
        d = [*tempGraph.getVertices()]
        self.prim(tempGraph, tempGraph.getVertex(d[0]))
        for vert in tempGraph:
            for neighbor in vert.getConnections():
                if neighbor.getPred() == vert:
                    # create mst with bi-directional edges
                    self.MST.addEdge(neighbor.getId(), vert.getId(), vert.getWeight(neighbor))
                    self.MST.addEdge(vert.getId(), neighbor.getId(), vert.getWeight(neighbor))

        pass

    def prim(self, G, start):
        pq = PriorityQueue() #queue to hold verts to be explored
        for v in G:
            v.setDistance(sys.maxsize)
            v.setPred(None)
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v) for v in G]) # build heap of all verts
        while not pq.isEmpty():
            currentVert = pq.delMin() # starting vert
            for nextVert in currentVert.getConnections(): # grabbing all neighbors of current vert
                newCost = currentVert.getWeight(nextVert)
                if nextVert in pq and newCost < nextVert.getDistance():
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.decreaseKey(nextVert, newCost)

    def findPath(self, router1, router2):
        l = []
        path = ''
        r1 = self.MST.getVertex(router1)
        self.dijkstra(self.MST, r1)
        r2 = self.MST.getVertex(router2)
        while r2.getPred() is not None and r2.getColor() == 'white' and r2.getId() != router1:
            r2.setColor('black')
            l.append(r2.getId())
            r2 = r2.getPred()
        l.append(r2.getId())
        self.resetMST()
        if router1 in l:
            l.reverse()
            for i in l:
                if i != router2:
                    path = path + i + ' -> '
                else:
                    path = path + i
        else:
            path ='path does not exist'

        return path





    def dijkstra(self, aGraph, start):
        pq = PriorityQueue()
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v) for v in aGraph])
        while not pq.isEmpty():
            currentVert = pq.delMin()
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() \
                          + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert, newDist)








    def findForwardingPath(self, router1, router2):
        pass

    def findPathMaxWeight(self, router1, router2):
        pass

    @staticmethod
    def nodeEdgeWeight(v):
        return sum([w for w in v.connectedTo.values()])

    @staticmethod
    def totalEdgeWeight(g):
        return sum([ISPNetwork.nodeEdgeWeight(v) for v in g]) // 2


if __name__ == '__main__':
    print("--------- Task1 build graph ---------")
    # Note: You should try all six dataset. This is just a example using 1221.csv
    net = ISPNetwork()
    net.buildGraph('data/1221.csv')

    print("--------- Task2 check if path exists ---------")
    routers = [v.id for v in random.sample(list(net.network.vertList.values()), 5)]
    for i in range(4):
        print('Router1:', routers[i], ', Router2:', routers[i + 1], 'path exist?:',
              net.pathExist(routers[i], routers[i + 1]))




    print("--------- Task3 build MST ---------")
    net.buildMST()
    print('graph node size', net.MST.numVertices)
    print('graph total edge weights', net.totalEdgeWeight(net.MST))

    print("--------- Task4 find shortest path in MST ---------")
    for i in range(4):
        print(routers[i], routers[i + 1], 'Path:', net.findPath(routers[i], routers[i + 1]))


    print("--------- Task5 find shortest path in original graph ---------")
    for i in range(4):
        print(routers[i], routers[i + 1], 'Path:', net.findForwardingPath(routers[i], routers[i + 1]))

    print("--------- Task6 find path in LowestMaxWeightFirst algorithm ---------")
    for i in range(4):
        print(routers[i], routers[i + 1], 'Path:', net.findPathMaxWeight(routers[i], routers[i + 1]))
