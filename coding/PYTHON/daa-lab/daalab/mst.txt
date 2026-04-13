import sys
def prim(n, edges):
    adj_list = {i: [] for i in range(n)}
    for u, v, weight in edges:
        adj_list[u].append((weight, v))
        adj_list[v].append((weight, u))
    mst = []
    visited = set()
    key = [sys.maxsize] * n
    parent = [-1] * n
    key[0] = 0
    for _ in range(n):
        u = min((i for i in range(n) if i not in visited), key=lambda x: key[x])
        visited.add(u)
        if parent[u] != -1:
            mst.append((parent[u], u, key[u]))
        for weight, v in adj_list[u]:
            if v not in visited and weight < key[v]:
                key[v] = weight
                parent[v] = u
    return mst, sum(key)
graph_edges = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15), (2, 3, 4)
]
nodes = 4
mst_edges, mst_weight = prim(nodes, graph_edges)
print("Minimum Spanning Tree Edges:", mst_edges)
print("Total Weight of MST:", mst_weight)