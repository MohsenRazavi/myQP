"""
in this implementation graph must be represented as adjacency matrix
"""

from copy import deepcopy

graph: [[int, int, ...]]
n = 5
dist = deepcopy(graph)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(dist)
