from WeightedGraph import Graph, Node
from queue import Queue
import random

# A* Search
def AStar(graph, src, dest, heuristic):
    path = []
    return path

# Testing Code
g = Graph()
for i in range(ord('A'), ord('K')):
    g.add_node(Node(chr(i)))

edges = ['AB', 'AE', 'BF', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
   g.add_edge(edge[:1], edge[1:], random.randint(0, 10))
heuristic = []

g.print()
print(AStar(g, 'A', 'B', heuristic))