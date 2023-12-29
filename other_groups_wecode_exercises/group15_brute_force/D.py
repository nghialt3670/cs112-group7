n, m, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
b = []

if n == 0: print(-1)
for i in range(n):
    a = [int(x) for x in input().split()]
    t = 0
    for i, k in enumerate(a):
        x = arr.index(k)
        arr = [arr[x]] + arr[:x] + arr[x + 1:]
        t += 1 + x
    print(t, end=' ')