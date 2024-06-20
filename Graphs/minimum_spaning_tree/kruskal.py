"""
code from: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
In this implementation graph must be represented edge list form [[node, node, weight], ...]
v: number of vertices

"""


def kruskal_mst(graph, num_vertices):
    def find(parent, i):
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    graph = sorted(graph, key=lambda edge: edge[2])
    result = []

    i = 0

    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = []
    rank = []

    for node in range(num_vertices):
        parent.append(node)
        rank.append(0)

    while e < num_vertices - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    minimum_cost = 0
    print("Edges in the constructed MST")
    for u, v, weight in result:
        minimum_cost += weight
        print("%d -- %d == %d" % (u, v, weight))
    print("Minimum Spanning Tree", minimum_cost)


g = [[0, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 0]]
kruskal_mst(g, 4)
