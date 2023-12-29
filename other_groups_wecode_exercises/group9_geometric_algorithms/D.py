import sys
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def CCW(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y)>0
def CW(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y)<0
def touch(a, b, c):
    return (b.x-a.x)*(c.y-a.y)-(c.x-a.x)*(b.y-a.y)==0

# with open('a.inp','r') as f1:
#     with open('a.out','w') as f2:
f1 = sys.stdin
f2 = sys.stdout
t = int(f1.readline())
for i in range(t):
    points = [x for x in map(int,f1.readline().split())]
    a = Point(points[0],points[1])
    b = Point(points[2],points[3])
    c = Point(points[4],points[5])
    if(touch(a,b,c)):
        f2.write("TOUCH\n")
    elif CCW(a,b,c):
        f2.write("LEFT\n")
    else:
        f2.write("RIGHT\n")