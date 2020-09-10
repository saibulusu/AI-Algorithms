from Graph import Graph, Node
from queue import Queue

# Breadth First Search
def bfs(graph, src, dest):
    if src not in graph.nodes or dest not in graph.nodes:
        return False
    queue = Queue()
    queue.put(src)
    done = []
    done.append(src)
    while (not queue.empty()):
        cur = queue.get()
        done.append(cur)
        if (cur is dest):
            return True
        for i in graph.nodes[cur].neighbors:
            if i not in done:
                queue.put(i)
    return False

# Testing Code
g = Graph()
for i in range(ord('A'), ord('K')):
    g.add_node(Node(chr(i)))

edges = ['AB', 'AE', 'BF', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
   g.add_edge(edge[:1], edge[1:])

print(bfs(g, 'A', 'C'))