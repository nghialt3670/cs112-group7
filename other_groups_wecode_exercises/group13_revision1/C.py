import sys
n = int(sys.stdin.readline())
a = [x for x in map(int,sys.stdin.readline().split())]
a = sorted(a)
s = int(sys.stdin.readline())
dp = [1000000000] * (s+1)
dp[0] = 0
for i in range(1,s+1):
    for j in range(n):
        if i-a[j]>=0:
            dp[i] = min(dp[i],dp[i-a[j]]+1)
        else:
            break
if(dp[s]!=1000000000):
    print(dp[s])
else:
    print(-1)