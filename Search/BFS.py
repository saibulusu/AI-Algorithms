from Graph import Graph, Node

def BFS(graph, src, dest):
    if src.name not in graph.nodes or dest.name not in graph.nodes:
        return False
    queue = []
    queue.put(src)
    done = []
    done.put(src)
    while (not queue.empty()):
        cur = queue.get()
        if (cur is dest):
            return True
        for i in cur.neighbors:
            if i not in done:
                queue.put(i)
    return False

g = Graph()
for i in range(ord('A'), ord('B')):
    g.add_node(Node(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

print(g)