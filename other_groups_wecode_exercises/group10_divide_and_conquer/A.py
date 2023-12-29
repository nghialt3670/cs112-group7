import math

points = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
    
min_d = float("inf")

for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        min_d = min([min_d, math.sqrt((math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)))])

print(min_d)