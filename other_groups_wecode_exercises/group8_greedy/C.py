n = int(input())
jobs = []
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    jobs.append((a,b))

jobs = sorted(jobs)
result = 0
time = 0
for job in jobs:
    time = time + job[0]
    result += job[1] - time
print(result)