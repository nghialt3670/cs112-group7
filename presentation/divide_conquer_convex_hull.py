import matplotlib.pyplot as plt
import random


def orientation(a, b, c):
    """
    Determine the orientation of three 2D points with order.
    If it is cloclwise then return 1,
    If it is counterclockwise then return -1
    If the points is colinear then return 0
    """
    # Calculate the cross product of vector ab and vector bc
    cross = (b[1]-a[1]) * (c[0]-b[0]) - (c[1]-b[1]) * (b[0]-a[0])
    if cross == 0: return 0
    if cross > 0: return 1
    return 1 if cross > 0 else -1


def merge_hulls(A, B):
    """
    Merge 2 convex hulls by finding their upper and lower tangent.
    The points in the merged convex hull are in counterclockwise order.
    """
    # Sizes of hull A and hull B
    n1, n2 = len(A), len(B)

    # Initialize index of the left most point in A and the right most point in B
    ia, ib = 0, 0
 
    # Find the left most point in A
    for i in range(1, n1):
        if A[i][0] > A[ia][0]:
            ia = i
 
    # Find the right most point in B
    for i in range(1, n2):
        if B[i][0] < B[ib][0]:
            ib = i

    # Find the upper tangent
    inda, indb = ia, ib
    done = 0
    while not done:
        done = 1
        while orientation(B[indb], A[inda], A[(inda+1) % n1]) > 0:
            # Traverse counterclockwise
            inda = (inda + 1) % n1
 
        while orientation(A[inda], B[indb], B[(n2+indb-1) % n2]) < 0:
            # Traverse clockwise
            indb = (indb - 1) % n2
            done = 0
 
    uppera, upperb = inda, indb

    # Find the lower tangent
    inda, indb = ia, ib
    done = 0
    while not done:  
        done = 1
        while orientation(A[inda], B[indb], B[(indb+1) % n2]) > 0:
            # Traverse counterclockwise
            indb = (indb + 1) % n2
 
        while orientation(B[indb], A[inda], A[(n1+inda-1) % n1]) < 0:
            # Traverse clockwise
            inda = (inda - 1) % n1
            done = 0
 
    lowera, lowerb = inda, indb

    # Traverse counterclockwise starting from upper a to find the merged convex hull
    merge_hull = []
    i = uppera
    merge_hull.append(A[uppera])
    while i != lowera:
        i = (i+1) % n1
        merge_hull.append(A[i])
 
    i = lowerb
    merge_hull.append(B[lowerb])
    while i != upperb:
        i = (i+1) % n2
        merge_hull.append(B[i])
        
    return merge_hull


def divide_conquer_hull(points):
    """
    Recursive function to find the convex hull using divide and conquer strategy
    """
    # If there are only 1 or 2 points then the convex hull of them is themself
    if len(points) <= 2:
        return points
    
    # If there are 3 points, all of them are the convex hull but return the points in clockwise order
    if len(points) == 3:
        points = sorted(points)
        if orientation(points[0], points[1], points[2]) < 0:
            return points
        else:
            return [points[0], points[2], points[1]]

    # Recursion part
    mid = len(points) // 2
    left_hull = divide_conquer_hull(points[:mid])
    right_hull = divide_conquer_hull(points[mid:])

    return merge_hulls(left_hull, right_hull)
    

def convex_hull(points):
    """
    Main function of finding the convex hull
    """
    # Sort all points base on x-coordinate
    points.sort()

    return divide_conquer_hull(points)


def generate_non_collinear_points(n, X, Y):
    """
    Generate set of points of size n of x-coordinate lines within X and y-coordinate lies within Y.
    Ensure no 3 points are collinear.
    """
    points = []
    while len(points) < n:
        # Generate a random point within the specified ranges.
        x = random.uniform(X[0], X[1])
        y = random.uniform(Y[0], Y[1])
        candidate = (x, y)

        # Check if the candidate point makes any existing 3 points collinear.
        is_collinear = False
        for i in range(len(points) - 2):
            p1, p2, p3 = points[i], points[i + 1], points[i + 2]
            # Check if the candidate point lies on the line defined by p1, p2, and p3.
            if abs((p2[1] - p1[1]) * (candidate[0] - p3[0]) - (p2[0] - p1[0]) * (candidate[1] - p3[1])) < 1e-6:
                is_collinear = True
                break

        if not is_collinear:
            points.append(candidate)

    return points


# Genarate points
x_range = (0, 1000)
y_range = (0, 1000)
num_points = 30
points = generate_non_collinear_points(num_points, x_range, y_range)

# Finding the convex hull
convex_hull = convex_hull(points)

# Visualize the points and convex hull
x, y = zip(*points)
hull_x, hull_y = zip(*convex_hull)

plt.scatter(x, y, color='blue')
plt.plot(hull_x + (hull_x[0],), hull_y + (hull_y[0],), color='red', linestyle='-')
plt.show()
