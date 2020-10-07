# Node that contains a list of neighbor nodes
class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = list()
	
	def add_neighbor(self, v, weight):
		if v not in self.neighbors:
			self.neighbors.append(
				{
					'NAME': v,
					'WEIGHT': weight
				}
			)
			return True
		else:
			return False

# Undirected Graph which contains nodes and edges between the nodes
class Graph:
	nodes = {}

	def add_node(self, v):
		if v.name not in self.nodes:
			self.nodes[v.name] = v
			return True
		else:
			return False

	def add_edge(self, v, u, weight):
		if v not in self.nodes or u not in self.nodes:
			return False
		for key, value in self.nodes.items():
			if key == v:
				value.add_neighbor(u, weight)
			if key == u:
				value.add_neighbor(v, weight)
		return True

	def get_neighbors(self, v):
		for node in self.nodes:
			if node.name == v:
				return node.neighbors
		return None

	def print(self):
		for i in sorted(list(self.nodes.keys())):
			print(i + str(self.nodes[i].neighbors))