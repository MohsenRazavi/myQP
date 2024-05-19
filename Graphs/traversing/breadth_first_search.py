"""
using queue
from collections import deque
q = deque()

graph is supposed to be implemented using adjacency list
visited is a dictionary which will be True for each visited node
visited = {node: False for node in nodes}

add first element to queue and make its visited True
"""


def bfs(graph, visited, queue, weighted=False):
    while queue:
        current = queue.popleft()
        """

        .... do anything you want ....

        """
        print(current)
        for neighbour in graph[current]:
            if weighted:
                neighbour = neighbour[0]
            if visited[neighbour]:
                continue
            visited[neighbour] = True
            queue.append(neighbour)
