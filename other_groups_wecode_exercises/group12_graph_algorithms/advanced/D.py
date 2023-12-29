import sys
def dfs(graph, visited, u):
    global ok
    # danh dau tham tren cuc bo
    visited[u] = True
    # danh dau tham tren toan cuc
    global_visited[u] = True
    for v in graph[u]:
        # neu chua tham toan cuc
        if not global_visited[v]:
            # tham dinh v
            check = dfs(graph, visited, v)
            if not check:
                return False
        elif visited[v]: # neu da tham toan cuc => neu tham cuc bo => tao vong
            return False
    # danh dau lai chua tham tren cuc bo
    visited[u] = False
    return True


testcase = int(sys.stdin.readline())
for test in range(1, testcase + 1):
    ok = True
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 10)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
    global_visited = [False] * (n+10)
    visited = [False] * (n + 10)
    for i in range(n):
        # neu chua tham thi tham tu dinh i
        if not global_visited[i+1]:
            # neu khong thoa man dieu kien thi luu lai bien ok va break
            if not dfs(graph,visited,i+1):
                ok = False
                break 
    # reset lai graph
    for i in range(n):
        graph[i+1].clear()
    if ok:
        print("YES")
    else:
        print("NO")