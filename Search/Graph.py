# Node that contains a list of neighbor nodes
class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = list()
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()
			return True
		else:
			return False

# Graph which contains nodes and edges between the nodes
class Graph:
	nodes = {}

	def add_node(self, v):
		if v.name not in self.nodes:
			self.nodes[v.name] = v
			return True
		else:
			return False
	
	def add_edge(self, v, u):
		if v not in self.nodes or u not in self.nodes:
			return False
		for key, value in self.nodes.items():
			if key == v:
				value.add_neighbor(u)
			if key == u:
				value.add_neighbor(v)
		return True
	
	def print(self):
		for i in sorted(list(self.nodes.keys())):
			print(i + str(self.nodes[i].neighbors))