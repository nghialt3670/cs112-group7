import sys
n = int(sys.stdin.readline())
a = [x for x in map(int,sys.stdin.readline().split())]
s = int(sys.stdin.readline())
dp = [0] * (s+1)
dp[0] = 1
for i in range(1,s+1):
    for j in range(n):
        if i-a[j]>=0:
            dp[i] += dp[i-a[j]]
print(dp[s])