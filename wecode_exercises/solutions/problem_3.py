import heapq

# define object with position, used voucher, best cost
class Pos:
    def __init__(self, pos, used, cost):
        self.pos = pos
        self.used = used
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

city_num, flight_num = map(int, input().split())
neighbors = [[] for _ in range(100010)]

def bfs():
    min_cost = [[int(1e14),int(1e14)] for _ in range(city_num)]
    min_cost[0] = [0,0]
    frontier = []
    heapq.heappush(frontier, Pos(0, False, 0))
    while frontier:
        curr = heapq.heappop(frontier)
        curr_cost = min_cost[curr.pos][curr.used]
                    
        if curr_cost != curr.cost:
            continue

        if curr.pos == city_num - 1:
            break

        for n, nc in neighbors[curr.pos]:
            # if we haven't used the discount yet, try using it now
            if not curr.used:
                new_cost = curr_cost + nc // 2
                if new_cost < min_cost[n][True]:
                    min_cost[n][True] = new_cost
                    heapq.heappush(frontier, Pos(n, True, new_cost))

            # but we can always just try the normal cost route
            if curr_cost + nc < min_cost[n][curr.used]:
                min_cost[n][curr.used] = curr_cost + nc
                heapq.heappush(frontier, Pos(n, curr.used, curr_cost + nc))

    print(min_cost[city_num - 1][True])

for _ in range(flight_num):
    from_city, to_city, cost = map(int, input().split())
    neighbors[from_city - 1].append((to_city - 1, cost))

bfs()
