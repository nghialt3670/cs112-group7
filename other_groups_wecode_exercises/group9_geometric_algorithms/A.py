import sys
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Line:
    def __init__(self,a,b):
        self.a = a
        self.b = b
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
    if touch(a,b,c) and onSegment(a,c,b):
        return True
    if touch(a,b,d) and onSegment(a,d,b):
        return True
    if touch(c,d,a) and onSegment(c,a,d):
        return True
    if touch(c,d,b) and onSegment(c,b,d):
        return True
    return CCW(a,c,d) != CCW(b,c,d) and CCW(a,b,c) != CCW(a,b,d)
def LineIntersect(l1,l2):
    return intersect(l1.a,l1.b,l2.a,l2.b)
input = sys.stdin
out = sys.stdout
n = int(input.readline())
lines = []
for _ in range(n):
    x1,y1,x2,y2 = map(int,input.readline().split())
    lines.append(Line(Point(x1,y1),Point(x2,y2)))
for i in range(1,min(2000,n)):
    for j in range(0,i):
        if(LineIntersect(lines[i],lines[j])):
            possibleLine = i
            checkIndex = j
            break
checkIntersect = False
for i in range(n):
    if i!=possibleLine and i!=checkIndex:
        if LineIntersect(lines[i],lines[checkIndex]):
            checkIntersect = True
            break
if checkIntersect:
    out.write('%s' % (checkIndex+1))
else:
    out.write('%s' % (possibleLine+1))