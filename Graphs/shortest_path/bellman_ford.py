"""
to use this algorithm graph must be represented as edge list
in undirected graphs consider the edge for two nodes
"""

# n is number of vertices
n = 5
distance = n * [float('inf')]
# x is the start node
x = 0
distance[x] = 0
graph = [(0, 1, 6), (1, 0, 6), (1, 2, 5), (2, 1, 5), (1, 3, 2), (3, 1, 2), (1, 4, 2), (4, 1, 2), (0, 3, 1), (3, 0, 1),
         (3, 4, 1), (4, 3, 1), (2, 4, 5), (4, 2, 5)]
for i in range(n + 1):
    negative_cycle = False
    for edge in graph:
        a, b, w = edge
        last_distance = distance[b]
        distance[b] = min(distance[b], distance[a] + w)
        if i == n:
            if distance[b] != last_distance:
                negative_cycle = True

