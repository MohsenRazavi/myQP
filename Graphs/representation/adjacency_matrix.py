
"""
graph[i][j] = 0 if i and are not connected else graph[i][j] = weight if graph is not weighted, graph[i][j] = 1
"""
n = 4

# unweighted
graph = [[0 for j in range(n)] for i in range(n)]
graph[0][1] = 1
graph[1][2] = 1
graph[1][3] = 1
graph[2][3] = 1
graph[3][0] = 1


# weighted
graph = [[0 for j in range(n)] for i in range(n)]
graph[0][1] = 5
graph[1][2] = 7
graph[1][3] = 6
graph[2][3] = 5
graph[3][0] = 2


