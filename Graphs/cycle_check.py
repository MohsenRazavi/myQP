"""
use dfs and check if one of current nodes neighbours is visited or not
"""


def dfs_cycle_check(graph, node, last_node, visited, weighted=False):
    if visited[node]:
        return False
    visited[node] = True
    for neighbour in graph[node]:
        if neighbour != last_node and visited[neighbour]:
            return True
    for neighbour in graph[node]:
        if weighted:
            return dfs_cycle_check(graph, neighbour[0], node, visited)
        else:
            return dfs_cycle_check(graph, neighbour, node, visited)

