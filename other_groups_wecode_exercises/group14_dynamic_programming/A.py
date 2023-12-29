import sys
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        left = []
        right = []
        st = []

        # Find nearest smaller to the left indices
        for i in range(n):
            if not st:
                left.append(-1)
            elif st and st[-1][0] < heights[i]:
                left.append(st[-1][1])
            else:
                while st and st[-1][0] >= heights[i]:
                    st.pop()

                if not st:
                    left.append(-1)
                else:
                    left.append(st[-1][1])
            st.append((heights[i], i))

        # Find nearest smaller to the right
        # Clear the stack as we're using the same stack
        st.clear()

        for i in range(n - 1, -1, -1):
            if not st:
                # If no smaller to left, push n
                right.append(n)
            elif st and st[-1][0] < heights[i]:
                right.append(st[-1][1])
            else:
                while st and st[-1][0] >= heights[i]:
                    st.pop()

                if not st:
                    right.append(n)
                else:
                    right.append(st[-1][1])
            st.append((heights[i], i))
        right = right[::-1]

        mxarea = 0
        for i in range(n):
            l = abs(i - left[i])
            r = abs(i - right[i])
            width = l + r - 1
            area = width * heights[i]
            mxarea = max(mxarea, area)

        return mxarea

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        arr = [0] * m
        maxarea = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    arr[j] += 1
                else:
                    arr[j] = 0

            area = self.largestRectangleArea(arr)
            maxarea = max(area, maxarea)

        return maxarea

n,m = map(int, sys.stdin.readline().split())
temp = n
n = m
m = temp
c = [] * n

for i in range(n):
    rows = list(map(int,input().split()))
    c.append(rows)
    
solution = Solution()
print(solution.maximalRectangle(c))