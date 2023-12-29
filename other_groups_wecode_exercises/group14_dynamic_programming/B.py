import sys
import bisect
class Solution:
    def canCross(self, stones):
        def can(ind, prev_step, stones, dp):
            if ind == len(stones) - 1:
                return True
            
            if dp[ind][prev_step] != -1:
                return dp[ind][prev_step]
            
            min_step = max(1, prev_step - 1)
            max_step = prev_step + 1
            
            ind1 = bisect.bisect_left(stones, stones[ind] + min_step)
            ind2 = bisect.bisect_right(stones, stones[ind] + max_step)
            
            res = False
            for i in range(ind1, ind2):
                res = res or can(i, stones[i] - stones[ind], stones, dp)
            
            dp[ind][prev_step] = res
            return res
        
        dp = [[-1] * len(stones) for _ in range(len(stones))]
        return can(0, 0, stones, dp)

n = sys.stdin.readline()
A = [x for x in map(int,sys.stdin.readline().split())]
solution = Solution()
result = solution.canCross(A)
print(result)