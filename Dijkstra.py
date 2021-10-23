from Graph import Graph, Vertex
from PriorityQueue import PriorityQueue

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)


if __name__ == '__main__':
    g = Graph()
    vals = ['a','b','c','d','e','f']
    for i in vals:
        g.addVertex(i)

    g.vertList
    g.addEdge('a', 'b', 1)
    g.addEdge('a', 'd', 3)
    g.addEdge('b', 'd', 1)
    g.addEdge('b', 'c', 5)
    g.addEdge('b', 'e', 4)
    g.addEdge('d', 'e', 2)
    g.addEdge('d', 'f', 7)
    g.addEdge('e', 'c', 1)
    g.addEdge('e', 'f', 4)
    g.addEdge('c', 'f', 2)
    dijkstra(g,g.getVertex('a'))
    searchV = g.getVertex('f')
    dist = 0
    while searchV.getPred() is not None:
        print(searchV.getDistance())
        dist += searchV.getDistance()

        searchV = searchV.getPred()
    print(dist)