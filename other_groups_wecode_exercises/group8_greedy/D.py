a,b,N,X = input().split()
a = int(a)
b = int(b)
N = int(N)
X = int(X)
if (a>=0 and b>=0):
    print(a*N+b*N)
elif (a<=0 and b<=0):
    print(0)
else:
    if(a<b):
        a,b = b,a
    if(abs(a)>=abs(b)):
        print(a*N+b*(N-X))
    else:
        print(a*X)