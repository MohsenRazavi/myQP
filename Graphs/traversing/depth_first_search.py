"""
graph is supposed to be implemented using adjacency list
visited is a dictionary which will be True for each visited node    
visited = {node: False for node in nodes}

pass first element to dfs as node
"""


def dfs(graph, node, visited, weighted=False):
    if visited[node]:
        return
    visited[node] = True
    """
    
    .... do anything you want ....
    
    """
    for neighbour in graph[node]:
        if weighted:
            dfs(graph, neighbour[0], visited)
        else:
            dfs(graph, neighbour, visited)

