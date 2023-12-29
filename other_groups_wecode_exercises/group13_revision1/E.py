import sys
class Solution:
    def FirstSolution(self,a):
        sum = a[0] + a[2*n-2]
        i = 1
        j = 2*n-3
        error = 0
        index = 0
        while(i<=j):
            if i==j:
                index = i
                break
            if a[i]+a[j]==sum:
                i += 1
                j -= 1
            elif a[i]+a[j]<sum:
                if error == 1:
                    error = 2
                    break
                else:
                    error = 1
                    index = i
                    i += 1
            else:
                if error == 1:
                    error = 2
                    break
                else:
                    error = 1
                    index = j
                    j -= 1
        if error == 2:
            return 10000000000
        else:
            return sum - a[index]
    def SecondSolution(self,a):
        sum = a[0] + a[2*n-3]
        i = 1
        j = 2*n-4
        while (i<j):
            if a[i]+a[j]!=sum:
                break
            else:
                i += 1
                j -= 1
        if i>=j:
            if sum - a[2*n-2] > 0:
                return sum - a[2*n-2]
            else:
                return 10000000000
        else:
            return 10000000000
    def ThirdSolution(self,a):
        sum = a[1] + a[2*n-2]
        i = 2
        j = 2*n-3
        while (i<j):
            if a[i]+a[j]!=sum:
                break
            else:
                i += 1
                j -= 1
        if i>=j:
            if sum - a[0] > 0:
                return sum - a[0]
            else:
                return 10000000000
        else:
            return 10000000000
        
            
        
k = int(input())
for i in range(k):
    n = int(input())
    a = []
    for x in map(int,sys.stdin.readline().split()):
        a.append(x)
    a = sorted(a)
    sys.stdout.write('Case #%s: ' % (i+1))
    if n==1:
        print(1)
        continue
    solution = Solution()
    result = min(solution.FirstSolution(a),solution.SecondSolution(a),solution.ThirdSolution(a))
    if result == 10000000000:
        print(-1)
    else:
        print(result)