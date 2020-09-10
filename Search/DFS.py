from Graph import Graph, Node

# Depth First Search
def dfs(graph, src, dest):
    if src not in graph.nodes or dest not in graph.nodes:
        return False
    stack = []
    stack.append(src)
    done = []
    while (stack):
        cur = stack.pop()
        print(cur)
        done.append(cur)
        if cur is dest:
            return True
        for i in graph.nodes[cur].neighbors:
            if i not in done and i not in stack:
                stack.append(i)
    return False

# Testing Code
g = Graph()
for i in range(ord('A'), ord('K')):
    g.add_node(Node(chr(i)))

edges = ['AB', 'AE', 'BF', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
   g.add_edge(edge[:1], edge[1:])

print(dfs(g, 'A', 'C'))