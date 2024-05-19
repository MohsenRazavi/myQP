n = 4

# unweighted
graph = {node: [] for node in range(1, n + 1)}
graph[1].append(2)
graph[2].extend([3, 4])
graph[3].append(4)
graph[4].append(1)

# weighted
graph = {node: [] for node in range(1, n + 1)}
"""
(target_node, weight)
"""
graph[1].append((2, 5))
graph[2].extend([(3, 7), (4, 6)])
graph[3].append((4, 5))
graph[4].append((1, 2))
