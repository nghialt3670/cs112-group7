class Solution:
    def __init__(self, nodes_count, connections) -> None:
        self.nodes_count = nodes_count
        self.connections = connections

    def solve(self):
        # cost function: f(x) = f(x) + h(x)
        # h(x) la tongchi phi nho nhat cua cac dinh chua di qua
        # f(x) la tong chi phi da dat duoc
        adjacency_list = {node: {} for node in range(1, self.nodes_count + 1)}

        for connection in self.connections:
            source, target, cost = connection
            adjacency_list[source][target] = cost
            adjacency_list[target][source] = cost

        def explore_route(route, visit_history, current_cost, current_location):
            nonlocal optimal_cost

            if len(route) == self.nodes_count:
                optimal_cost = min(optimal_cost, current_cost)
                return

            for neighbor, weight in adjacency_list[current_location].items():
                if not visit_history[neighbor]:
                    visit_history[neighbor] = True
                    explore_route(route + [neighbor], visit_history, current_cost + weight, neighbor)
                    visit_history[neighbor] = False

        optimal_cost = float('inf')
        starting_point = 1
        visited_nodes = [False] * (self.nodes_count + 1)
        visited_nodes[starting_point] = True
        explore_route([starting_point], visited_nodes, 0, starting_point)

        if optimal_cost == float('inf'):
            print("-1")
        else:
            print(optimal_cost)


def main():
    nodes, edges = map(int, input().split())
    connections_list = [list(map(int, input().split())) for _ in range(edges)]
    solution = Solution(nodes, connections_list)
    solution.solve()


if __name__ == "__main__":
    main()