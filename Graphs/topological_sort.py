def topological_sort(graph, weighted=False):
    def dfs(graph, node, visited, weighted=weighted):  # noqa
        if visited[node]:
            return
        visited[node] = True
        for neighbour in graph[node]:
            if weighted:
                dfs(graph, neighbour[0], visited)
            else:
                dfs(graph, neighbour, visited)
        ans.append(node)

    v = len(graph)
    visited = {node: False for node in range(v)}
    ans = []
    for i in range(v):
        if not visited[i]:
            dfs(graph, i, visited, weighted)
    ans = ans[::-1]
    return ans
