import sys

#thuat toan duong mo
def dfs(u): # tim mot duong mo tu dinh nhat i ben X, ket thuc o dinh nhat j ben Y
    for v in range(1,n+1):
        if graph[u][v]==True and trace[v]==0:
            trace[v] = u
            global p
            p = v
            if B[v] == 0 or dfs(B[v]):
                return True
    return False
def trace_back(): # doi mau cac canh tren duong mo de tang so canh cua cap ghep
    global p
    while(p):
        x = trace[p]
        y = p
        p = A[x]
        A[x] = y
        B[y] = x 
        
def find(): 
    for i in range(1,n+1):
        trace[i] = 0
    for i in range(1,n+1): # duyet cac dinh nhat ben X lam diem xuat phat cua duong mo
        if(A[i] == 0):
            if(dfs(i)): # de quy keo dai duong mo
                return True
    return False
n = int(sys.stdin.readline())
first_half = []
second_half = []
first_half.append((0,0,0))
second_half.append((0,0))
graph = [[False] * (n+10) for i in range(n+10)]
trace = [0] * (n+10)
p = 0
A = [0] * (n+10)
B = [0] * (n+10)
for _ in range(n):
    x, y, range_cover = map(int,sys.stdin.readline().split())
    first_half.append((x,y,range_cover))
for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    second_half.append((x,y))
    
for i in range(1,n+1):
    for j in range(1,n+1):
        # tim cac canh noi voi nhau cua do thi
        if (abs(first_half[i][0]-second_half[j][0])+abs(first_half[i][1]-second_half[j][1]) <= first_half[i][2]):
            graph[i][j] = True
            

while(find()):
    trace_back()

result = 0
for i in range(1,n+1):
    if(A[i]):
        result += 1

print(result)