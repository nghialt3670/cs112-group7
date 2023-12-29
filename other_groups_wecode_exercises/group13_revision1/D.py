import sys
class Solution:
    def count_ope(self, a, index, val):
        if index >= n:
            return int(1e10)
        elif a[index] >= val:
            return 0
        else:
            return val - a[index] + self.count_ope(a,index+1,val-1)
    def bin_search(self, a, val):
        for i in range(n):
            if self.count_ope(a,i,val) <= k:
                return True
        return False
                
    def calculate(self, a):
        left = 1
        right = 2*int(1e18)
        ans = 1
        while(left<=right):
            mid = int((left+right)/2)
            if self.bin_search(a,mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1     
        return ans
                
t = int(input())
for _ in range(t):
    n, k = map(int,sys.stdin.readline().split())
    a = [x for x in map(int,sys.stdin.readline().split())]
    solution = Solution()
    print(solution.calculate(a))