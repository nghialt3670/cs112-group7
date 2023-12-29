import math

n = int(input())
pair = []
for i in range(n):
    a,b = input().split()
    pair.append((int(a),int(b)))
    
pair = sorted(pair, key = lambda x : x[1])
cur_pair = pair[0]
count = 1 
for p in pair[1:]:
    if cur_pair[1] <= p[0]:
        cur_pair = p
        count += 1
print(count)