import sys
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def CCW(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y)>0
def touch(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y)==0
def onSegment(a, b, c): 
    if ( (b.x <= max(a.x, c.x)) and (b.x >= min(a.x, c.x)) and 
           (b.y <= max(a.y, c.y)) and (b.y >= min(a.y, c.y))): 
        return True
    return False
def intersect(a,b,c,d):
    return CCW(a,c,d) != CCW(b,c,d) and CCW(a,b,c) != CCW(a,b,d)

# with open('a.inp','r') as f1:
#     with open('a.out','w') as f2:
f1 = sys.stdin
f2 = sys.stdout
n,m = f1.readline().split()
n = int(n)
m = int(m)
points  = []
for i in range(n):
    x,y = f1.readline().split()
    x = int(x)
    y = int(y)
    points.append(Point(x,y))

for _ in range(m):
    x,y = f1.readline().split()
    x = int(x)
    y = int(y)
    temp = Point(x,y)
    infinityPoint = Point(1000000000,y)
    boundary = False
    intersects = 0
    for i in range(1,n+1):
        if touch(points[i-1],points[i%n],temp) and onSegment(points[i-1],temp,points[i%n]):
                boundary = True
                break
        elif intersect(temp,infinityPoint,points[i-1],points[i%n]):
            intersects += 1
    if boundary:
        f2.write("BOUNDARY\n")
    elif intersects % 2==1 :
        f2.write("INSIDE\n")
    else:
        f2.write("OUTSIDE\n")