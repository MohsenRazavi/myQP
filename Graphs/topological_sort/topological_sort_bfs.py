"""
code from : https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

"""

from collections import deque


def topological_sort(adj, V):
    indegree = {}
    for node in adj:
        for vertex in adj[node]:
            try:
                indegree[vertex] += 1
            except KeyError:
                indegree[vertex] = 1
        if node not in indegree:
            indegree[node] = 0

    q = deque()
    for node in adj:
        if indegree[node] == 0:
            q.append(node)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            if indegree[adjacent] == 0:
                q.append(adjacent)
    return result


adj = {'A': ['B', 'C'], 'C': ['I', ], 'B': ['D', 'E'], 'I': ['E', ], 'D': ['G', ], 'E': ['F', ], 'F': ['G', ], 'G': []}
print(topological_sort(adj, 8))
