# graph : create an adjacency list

class vertex:

	def __init__(self,key):
		self.id = key
		self.connections = {}

	def addNeighbor(self,node,wt):
		self.connections[node] = wt

	def deleteNeighbor(self,node):
		if node not in self.connections:
			return False
		else:
			del self.connections[node]

	def getNeighbors(self):
		return self.connections.keys()
	
	def getId(self):
		return self.id

	def getWeight(self,wt):
		return self.connections[wt]

class graph:

	def __init__(self):
		self.adjList = {}

	def getVertex(self,n):		
		return self.adjList[n] if n in self.adjList else None

	def addVertex(self,val):
		newnode = vertex(val)
		self.adjList[val] = newnode
		return newnode
	
	def addEdge(self,v1,v2,cost=0, bidirectional= True):
		if v1 not in self.adjList:
			self.addVertex(v1)
		if v2 not in self.adjList:
			self.addVertex(v2)
		self.adjList[v1].addNeighbor(self.adjList[v2],cost)
		if bidirectional:
			self.adjList[v2].addNeighbor(self.adjList[v1],cost)

	def getVertices(self):
		return self.adjList.keys()

	def deleteEdge(self, v1, v2,bidirectional=True):
		if v1 not in self.adjList.keys() or v2 not in self.adjList.keys():
			return False
		else:
			self.adjList[v1].deleteNeighbor(v2)
			if bidirectional:
				self.adjList[v2].deleteNeighbor(v1)

			return True

def createGraph():
	
	g = graph()

	v = 7

	for i in range(0,v):
		g.addVertex(i)

	# for i in range(0,v):
	# 	print g.getVertex(i).id

	g.addEdge(0,1,5)
	g.addEdge(0,2,5)
	g.addEdge(1,3,4)
	g.addEdge(3,4,1)
	g.addEdge(4,2,2)
	g.addEdge(5,6,3)
	g.addEdge(4,6,2)

	for node in g.getVertices():
		for w in g.getVertex(node).getNeighbors():
			print node, w.getId() 

	#delete an edge
	g.deleteEdge(4,2,False)
	
	print "The graph after deleting an edge" 
	
	for node in g.getVertices():
		for w in g.getVertex(node).getNeighbors():
			print node, w.getId()
createGraph()



