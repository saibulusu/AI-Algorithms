from WeightedGraph import Graph, Node
from queue import Queue
import random
import heapq

# A* Search
def AStar(graph, src, dest, h):
   goal = 'J'
   OPEN = []
   CLOSE = []
   heapq.heappush(OPEN, (h[src] + 0, src, (0, h[src], -1)))
   while OPEN:
      cur = heapq.heappop(OPEN)
      CLOSE.append(cur)
      if graph.nodes[cur[1]].name == goal:
         final = cur
         break
      succs = graph.nodes[cur[1]].neighbors
      for succ in succs:
         s = succ['NAME']
         w = succ['WEIGHT']
         inOpen = False
         inClose = False
         for o in OPEN:
            if o[1] == s:
               inOpen = True
               if o[2][0] > cur[2][0] + w:
                  o = (h[s] + cur[2][0] + w, s, (cur[2][0] + w, h[s], len(CLOSE) - 1))
         for c in CLOSE:
            if c[1] == s:
               inClose = True
               if c != -1 and c[2][0] > cur[2][0] + w:
                  c = -1
                  heapq.heappush(OPEN, (h[s] + cur[2][0] + w, s, (cur[2][0] + w, h[s], len(CLOSE) - 1)))
               elif c != -1 and c[2][0] <= cur[2][0] + w:
                  continue
         if not inOpen and not inClose:
            heapq.heappush(OPEN, (h[s] + cur[2][0] + w, s, (cur[2][0] + w, h[s], len(CLOSE) - 1)))
   path = [final]
   moves = final[0]
   for i in range(0, moves):
      final = CLOSE[final[2][2]]
      path.append(final)
   return path

# Testing Code
g = Graph()
for i in range(ord('A'), ord('K')):
   g.add_node(Node(chr(i)))

edges = ['AB', 'AE', 'CE', 'BF', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
i = 1
for edge in edges:
   g.add_edge(edge[:1], edge[1:], i)
   i += 1
heuristic = {'A': 3, 'B': 2, 'C': 5, 'D': 4, 'E': 4, 'F': 1, 'G': 1, 'H': 3, 'I': 2, 'J': 0}

g.print()
print(AStar(g, 'A', 'I', heuristic))