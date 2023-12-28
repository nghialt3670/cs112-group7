# Read input values N and M
N, M = map(int, input().split())

# Initialize lists to store tree and cylinder coordinates
trees = []
cylinders = []

# Read tree coordinates and append to the 'trees' list
for i in range(N):
    x, y = map(int, input().split())
    trees.append([x, y])

# Read cylinder coordinates and append to the 'cylinders' list
for i in range(M):
    x, y = map(int, input().split())
    cylinders.append([x, y])

# Function to determine orientation of three points (p, q, r)
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear points
    return 1 if val > 0 else -1  # Clockwise or counterclockwise

# Function to compute the convex hull using the Monotone Chain algorithm
def monotone_chain(points):
    n = len(points)
    if n < 3:
        return points  # Convex hull is not possible with less than 3 points

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

    # Concatenate lower and upper hulls to get the convex hull
    convex_hull = lower_hull[:-1] + upper_hull[:-1]

    return convex_hull

# Compute the convex hull of cylinders using the Monotone Chain algorithm
convex_hull = monotone_chain(cylinders)

# Sort the convex hull points lexicographically
convex_hull = sorted(convex_hull, key=lambda point: (point[0], point[1]))

# Print the convex hull points
for x, y in convex_hull:
    print(x, y)
