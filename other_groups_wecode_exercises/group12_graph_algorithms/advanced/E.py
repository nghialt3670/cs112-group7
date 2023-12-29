import sys

st = []
time = 0
# thuat toan Tarjan
def dfs(u):
    global time
    time += 1
    num[u] = low[u] = time
    st.append(u)
    for v in graph[u]:
        if deleted[v]:
            continue
        if not num[v]:
            dfs(v)
            low[u] = min(low[u], low[v])
        else:
            low[u] = min(low[u], num[v])
    if low[u] == num[u]:
        global scc
        scc += 1
        # luu lai cac thanh phan lien thong manh
        v = st[len(st)-1]
        trace[scc].append(v)
        st.pop()
        deleted[v] = True
        while v!=u:
            v = st[len(st)-1]
            trace[scc].append(v)
            st.pop()
            deleted[v] = True

scc = 0
n = int(sys.stdin.readline())
value = [x for x in map(int, sys.stdin.readline().split())]
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+10)]
low = [0] * (n+10)
num = [0] * (n+10)
deleted = [False] * (n+10)
trace = [[] for _ in range(n+10)]
mod  = 1000000007
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    
for i in range(n):
    if not num[i+1]:
        dfs(i+1)
        
result = 0
ways_result = 1
for i in range(1,scc+1):
    mininum = 10000000000
    count = 0
    # lay diem co gia tri nho nhat va so diem co gia tri nho nhat
    for x in trace[i]:
        if value[x-1] < mininum:
            mininum = value[x-1]
            count = 1
        elif value[x-1] == mininum:
            count += 1
    # cong vao ket qua gia tri nho nhat
    result += mininum
    # so diem co gia tri nho nhat tuong ung voi so cach
    ways_result *= count
    if ways_result > mod:
        ways_result %= mod

sys.stdout.write('%s %s' % (result,ways_result))