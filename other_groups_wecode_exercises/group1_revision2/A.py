n = int(input())

home = [0]*(10**5+1)
temp = []
result = [(n-1)]*n

for i in range(n):
  x, y = map(int, input().split())
  temp.append((x,y))
  home[x] += 1

for i in range(n):
  result[i] += home[temp[i][1]]

for i in result:
  print(i, 2*n - 2 - i)