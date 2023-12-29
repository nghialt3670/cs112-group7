def kruskalMST(graph: list, n_vertices: int):
    root = [i for i in range(n_vertices)]
    rank = [1 for i in range(n_vertices)]

    def find_set(vertex):
        nonlocal root
        if root[vertex] == vertex:
            return vertex
        root[vertex] = find_set(root[vertex])
        return root[vertex]

    def join_sets(vertex_1, vertex_2):
        nonlocal root, rank
        set_v1 = find_set(vertex_1)
        set_v2 = find_set(vertex_2)
        if set_v1 == set_v2:
            return
        if rank[set_v1] < rank[set_v2]:
            root[set_v1] = set_v2
        elif rank[set_v2] < rank[set_v1]:
            root[set_v2] = set_v1
        else:
            root[set_v2] = set_v1
            rank[set_v1] += 1

    def kruskal_main():
        nonlocal graph, root, rank
        graph.sort(key=lambda x: x[2])  # Sort the edges by weight
        total_weight = 0
        n_edges_selected = 0

        for edge in graph:
            v1, v2, weight = edge
            if find_set(v1) != find_set(v2):
                total_weight += weight
                join_sets(v1, v2)
                n_edges_selected += 1

            if n_edges_selected == n_vertices - 1:
                return total_weight

    return kruskal_main()

graph = []
n_vertices = int(input())
vertex_1, vertex_2, weight = map(int, input().split())
while vertex_1 != -1:
    graph.append((min(vertex_1, vertex_2), max(vertex_1, vertex_2), weight))
    vertex_1, vertex_2, weight = map(int, input().split())
weight = kruskalMST(graph, n_vertices)
print(weight)