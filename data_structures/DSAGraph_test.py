from DSAGraph import *

gg = DSAGraph()

gg.addVertex('A')

gg.addVertex('B')

gg.addVertex('C')

gg.addEdge('A', 'B', False)

gg.addEdge('A', 'C', False)

gg.addEdge('B', 'C', False)

gg.getVertex('A').setVisited(True)
gg.getVertex('B').setVisited(True)
gg.getVertex('C').setVisited(True)

print('testing hasUnvisited')
print(gg.hasUnvisited('A'))
print(len(gg.getVertex('B')._links))

print('unvisited')
print(gg.getUnvisited('C'))

print('depth first')
print(gg.depthFirst())

print()

print('DRIVER CODE')
print('==========================')

print('Vertices')
print(gg.getVertexLabels())

print()

print('Vertice Object List (ordered)')
print(gg.getVertices())

print()

print('Links')
gg.printAdjList()

print()

print('Adjacency Matrix')
print(gg.adjMatrix())


print()
print()

gg = DSAGraph()

gg.addVertex('A')
gg.addVertex('B')
gg.addVertex('C')
gg.addVertex('D')
gg.addVertex('E')
gg.addVertex('F')
gg.addVertex('G')
gg.addVertex('H')
gg.addVertex('I')


gg.addEdge2('A', 'B', ['',4], False)
gg.addEdge2('A', 'H', ['',8], False)
gg.addEdge2('B', 'H', ['',11], False)
gg.addEdge2('B', 'C', ['',8], False)
gg.addEdge2('C', 'D', ['',7], False)
gg.addEdge2('C', 'I', ['',2], False)
gg.addEdge2('C', 'F', ['',4], False)
gg.addEdge2('D', 'F', ['',14], False)
gg.addEdge2('D', 'E', ['',9], False)
gg.addEdge2('E', 'F', ['',10], False)
gg.addEdge2('F', 'G', ['',2], False)
gg.addEdge2('G', 'I', ['',6], False)
gg.addEdge2('G', 'H', ['',1], False)
gg.addEdge2('H', 'I', ['',7], False)

print("Kruskals Algorithm")

test = gg.kruskalsAlgorithm(1)

for i in test.getEdges():
	print(i, 'end')

print()
