"""

suppose two colors X, Y are given

at each node color its neighbour to X, then color neighbour of its neighbour to Y and so on.

here I show colored nodes in visited dictionary, any value except False shows color
"""

colors = ['X', 'Y']


def dfs_bipartiteness_check(graph, node, visited, color=0, weighted=False):
    if visited[node] and visited[node] == colors[not color]:
        return False
    if visited[node]:
        return True

    for neighbour in graph[node]:
        visited[neighbour] = colors[color]

    for neighbour in graph[node]:
        if weighted:
            return dfs_bipartiteness_check(graph, neighbour[0], visited, color=not color)
        else:
            return dfs_bipartiteness_check(graph, neighbour, visited, color=not color)


