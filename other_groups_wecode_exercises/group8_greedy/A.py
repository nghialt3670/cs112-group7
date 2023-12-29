n,k = input().split()
n = int(n)
k = int(k)
items = []
def kiemtra(need):
    p = [0] * n
    for i in range(n):
        p[i] = items[i][0] - need*items[i][1]
    p = sorted(p,reverse=True)
    sum = 0
    for i in range(k):
        sum += p[i]
    if(sum >= 0):
        return True
    return False

for i in range(n):
    w,v = input().split()
    v = int(v)
    w = int(w)
    items.append((v,w))

l = 0; r = 1e11; ans = 0
while(l<=r):
    mid = int((l+r)/2)
    if(kiemtra(mid)):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1
print(ans)