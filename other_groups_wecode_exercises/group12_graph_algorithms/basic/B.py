import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest paths from a starting node to all other nodes in a weighted graph.
    Parameters:
    - graph: dictionary representing the graph where keys are nodes and values are dictionaries of neighboring nodes
            along with corresponding edge weights. Example: {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2}, ...}
    - start: starting node for the shortest path calculations
    Return: dictionary with nodes as keys and their respective shortest distances from the start node as values
    """
    # create a min heap (priority queue) to keep track of nodes and their current shortest distances.
    priority_queue = [(0, start)]  # (distance, node)
    
    # create a dictionary (shortest_distances) to store the current known shortest distances from the start node to all other nodes. 
    # initialize all distances to infinity except for the start node, which is set to 0.
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    # while there are nodes in the priority queue
    while priority_queue:
        # pop the node head (which has smallest current distance)
        current_distance, current_node = heapq.heappop(priority_queue)

        # if the current distance is greater than the known shortest distance for the current node, skip the iteration.
        if current_distance > shortest_distances[current_node]:
            continue

        # iterate through the neighbors of the current node.
        for neighbor, edge_weight in graph[current_node].items():
            # calculate the distance to each neighbor via the current node.
            distance = current_distance + edge_weight

            # If the calculated distance is shorter than the known shortest distance to the neighbor,
            if distance < shortest_distances[neighbor]:
                # update the shortest distance
                shortest_distances[neighbor] = distance
                # add the neighbor to the priority queue.
                heapq.heappush(priority_queue, (distance, neighbor))

    # Once the priority queue is empty, the algorithm has computed the shortest distances from the start node to all other nodes.
    return shortest_distances

graph = {}
n_vertices = int(input())
while True:
    input_list = input().split()
    if input_list == ['-1', '-1', '-1']:
        break
    x, y, w = map(int, input_list)
    if x not in graph:
        graph[x] = {y: w}
    else:
        graph[x][y] = w
    if y not in graph:
        graph[y] = {x: w}
    else:
        graph[y][x] = w 

start = int(input())
result = dijkstra(graph, start)
for i in range(n_vertices):
    print(result[i])