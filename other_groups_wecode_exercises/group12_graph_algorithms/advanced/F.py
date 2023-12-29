import sys

time = 0
# thuat toan Tarjan tim cau
def dfs(u,pre):
    global time
    time += 1
    num[u] = low[u] = time
    for v in graph[u]:
        if v == pre:
            continue
        if not num[v]:
            dfs(v,u)
            low[u] = min(low[u], low[v])
            if low[v]==num[v]:
                global cau
                cau += 1
        else:
            low[u] = min(low[u], num[v])

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+10)]
num = [0] * (n+10)
low = [0] * (n+10)
while(True):
    u, v = map(int, sys.stdin.readline().split())
    if u==-1:
        break
    graph[u].append(v)
    graph[v].append(u)
cau = 0
for i in range(n):
        if not num[i]:
            dfs(i,i)
print(cau)