N, M = map(int, input().split())
trees = []

for i in range(N):
    x, y = map(int, input().split())
    trees.append([x, y])

cylinders = []
for i in range(M):
    x, y = map(int, input().split())
    cylinders.append([x, y])

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def monotone_chain(points):
    n = len(points)
    if n < 3:
        return points

    # Sort the points lexicographically
    points = sorted(points)

    # Build lower hull
    lower_hull = []
    for p in points:
        while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], p) != -1:
            lower_hull.pop()
        lower_hull.append(p)

    # Build upper hull
    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) != -1:
            upper_hull.pop()
        upper_hull.append(p)

    # Concatenate lower and upper hulls
    convex_hull = lower_hull[:-1] + upper_hull[:-1]

    return convex_hull


convex_hull = monotone_chain(cylinders)
convex_hull = sorted(convex_hull, key=lambda point: (point[0], point[1]))

for x, y in convex_hull:
    print(x, y)

