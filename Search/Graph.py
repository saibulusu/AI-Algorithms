class Node:
	neighbors = list()

	def __init__(self, name):
		self.name = name
	
	def add_neighbor(self, v):
		if v not in neighbors:
			self.neighbors.append(v)
			return True
		else:
			return False

class Graph:
	nodes = {}

	def add_node(self, v):
		if v.name not in self.nodes:
			self.nodes[v.name] = v
			return True
		else:
			return False
	
	def add_edge(self, v, u):
		if v not in self.nodes.keys or u not in self.nodes.keys:
			return False
		for i in nodes:
			if i == v:
				i.add_neighbor(u)
			if i == u:
				i.add_neighbor(v)
		return True
	
	def print(self):
		for i in self.nodes.keys():
			print(i + str(self.nodes[i].neighbors))