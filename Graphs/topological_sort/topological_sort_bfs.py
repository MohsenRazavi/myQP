"""
code from : https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

"""

from collections import deque


def topological_sort(adj, V):
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            if indegree[adjacent] == 0:
                q.append(adjacent)

    if len(result) != V:
        print("Graph contains cycle!")
        return []
    return result
