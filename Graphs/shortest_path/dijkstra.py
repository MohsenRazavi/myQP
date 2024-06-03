"""
in this implementation graph must be represented as adjacency list
in undirected graphs consider the edge for two nodes
"""

import heapq

# n is number of nodes
n = 5
distance = [float('inf')] * n
# x is start node
x = 0
distance[x] = 0
q = [(0, x)]
processed = [False] * n
graph = {0: [(1, 6), (3, 1)], 1: [(0, 6), (3, 2), (2, 5), (4, 2)], 2: [(4, 5), (1, 5)], 3: [(1, 2), (4, 1), (0, 1)],
         4: [(2, 5), (3, 1), (1, 2)]}
while q:
    _, a = heapq.heappop(q)
    if processed[a]:
        continue
    processed[a] = True
    for b, w in graph[a]:
        if distance[a] + w < distance[b]:
            distance[b] = distance[a] + w
            heapq.heappush(q, (distance[b], b))

print(distance)
