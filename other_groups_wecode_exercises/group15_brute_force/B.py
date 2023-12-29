n, m = input().split()
n =int(n)
m=int(m)
s = input()
length = 0
for i in range(len(s)):
    if(s[i]=='q' or s[i]=='w' or s[i]=='e' or s[i]=='r'):
        length+=1
dem = [0] * 200
p=[]
cnt = 0
p = [int(j) for j in input().split()]
for i in range(m):
    if  length==p[i]:
        break
    while p[i] > 0:
        dem[ord(s[cnt])] += 1
        cnt += 1
        p[i] -= 1
    cnt = 0

for i in range(len(s)):
    dem[ord(s[i])] += 1

print(dem[ord('q')], dem[ord('w')], dem[ord('e')], dem[ord('r')])