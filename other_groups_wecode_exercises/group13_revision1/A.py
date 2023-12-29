import sys
def swap(a,b):
    temp = a
    a = b
    b = temp
a,b,c,d = map(int,sys.stdin.readline().split())
if a>b:
    swap(a,b)
if c>d:
    swap(c,d)
if c<a:
    swap(a,c)
    swap(b,d)
print(max(0,min(b,d)-max(a,c)))