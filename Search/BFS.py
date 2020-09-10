from Graph import Graph, Node
from queue import Queue

# Breadth First Search
def bfs(graph, src, dest):
    if src not in graph.nodes or dest not in graph.nodes:
        return False
    queue = []
    queue.append(src)
    index = 0
    while (True):
        if (index >= len(queue)):
            return False
        cur = queue[index]
        print(cur)
        index += 1
        if cur is dest:
            return True
        for i in graph.nodes[cur].neighbors:
            if i not in queue:
                queue.append(i)

# Testing Code
g = Graph()
for i in range(ord('A'), ord('K')):
    g.add_node(Node(chr(i)))

edges = ['AB', 'AE', 'BF', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
   g.add_edge(edge[:1], edge[1:])

print(bfs(g, 'A', 'H'))