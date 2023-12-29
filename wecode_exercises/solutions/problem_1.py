import sys
inp = sys.stdin
n, m = map(int, inp.readline().split())
res = 0
sumL = [0] * (m+1)
sumR = [0] * (m+1)

for _ in range(n):
    l, r, s = map(int, inp.readline().split())
    sumL[r] += s
    sumR[l] += s

for i in range(2, m + 1): # calculate sum of points if we eat all the dishes from 1 to i
    sumL[i] += sumL[i - 1]

for i in range(m - 1, 0, -1): # calculate sum of points if we eat all the dishes from i to m  
    sumR[i] += sumR[i + 1]

for i in range(1, m + 1):
    res = max(res, sumL[i - 1] + sumR[i + 1]) # leave the ith-dish

print(res)