import sys
class Solution:
    def MaxProfitDp(self,prices):
        for k in range(1,3):
            minn = prices[0]
            for i in range(1,len(prices)):
                if minn > prices[i] - dp[k-1][i-1]:
                    minn = prices[i] - dp[k-1][i-1]
                if dp[k][i-1] > prices[i] - minn:
                    x = dp[k][i-1]
                    dp[k][i] = x
                else:
                    dp[k][i] = prices[i] - minn
                dp[0][i] = 0
        return dp[2][len(prices) - 1]
    
n = int(input())
prices = [x for x in map(int,sys.stdin.readline().split())]
dp = [] * 3
for _ in range(0,3):
    a = []
    for j in range(len(prices)):
        a.append(0)
    dp.append(a)
solution = Solution()
print(solution.MaxProfitDp(prices))