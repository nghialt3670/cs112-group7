from collections import defaultdict
from queue import Queue

def DFS(graph: defaultdict(list), start: int, visited=None) -> None:
    if visited is None: 
        visited = set()

    print(start, end=" ")
    visited.add(start)
    for v in graph[start]:
        if v not in visited:
            DFS(graph, v, visited)


def BFS(graph: defaultdict(list), start: int) -> None:
    visited = set()
    q = Queue()
    print(start, end=" ")
    q.put(start)
    visited.add(start)
    while not q.empty():
        f = q.get()
        for v in graph[f]:
            if v not in visited:
                print(v, end=" ")
                q.put(v)
                visited.add(v)

    
T = int(input()) #number of test cases
while T:
    n = int(input()) #number of edges
    edge_list = []
    for _ in range(n):
        x, y = map(int, input().split())
        edge_list.append([x, y])
    graph = defaultdict(list) #edge adjacency list
    for edge in edge_list:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    start = int(input()) #node start
    print("DFS: ")
    DFS(graph, start)
    print()
    print("BFS: ")
    BFS(graph, start)
    print()
    T -= 1