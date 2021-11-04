
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
        self.resetGraph()
        return b

    def resetGraph(self):
        for i in self.network:
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
        d = [*self.network.getVertices()]
        self.prim(self.network.getVertex(d[0]))
        pass

    def prim(self, start):
        visited = []
        self.MST = self.network
        pq = PriorityQueue()
        for v in self.MST:
            v.setDistance(sys.maxsize)
            v.setPred(None)
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v) for v in self.MST])
        while not pq.isEmpty():
            currentVert = pq.delMin()
            visited.append(currentVert)
            for nextVert in currentVert.getConnections():
                newCost = currentVert.getWeight(nextVert)
                if nextVert in pq and newCost < nextVert.getDistance() and nextVert not in visited:
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.decreaseKey(nextVert, newCost)

    def findPath(self, router1, router2):
        pass

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
