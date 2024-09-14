import heapq

class AStar:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}

    def add_edge(self, node_a, node_b, weight):
        # Add an edge from node_a to node_b with weight
        self.graph[node_a].append((node_b, weight))

    def heuristics(self, node, goal):        
        # Euclidean distance
        return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

    def find_path(self, start_node, goal_node):
        # Initialize g- and f-scores
        g_scores = {node: float("inf") for node in self.nodes}
        g_scores[start_node] = 0

        f_scores = {node: float("inf") for node in self.nodes}
        f_scores[start_node] = self.heuristics(start_node, goal_node)

        # Initialize open list and closed set
        open_list = []
        heapq.heappush(open_list, (f_scores[start_node], start_node))
        closed_set = set()

        came_from = {}

        while open_list:
            current = heapq.heappop(open_list)[1]

            # If the node has already been processed, skip it
            if current in closed_set:
                continue
            closed_set.add(current)

            if current == goal_node:
                return self.reconstruct_path(came_from, current, g_scores[goal_node])

            for neighbor, weight in self.graph[current]:
                tentative_g_score = g_scores[current] + weight

                if neighbor in closed_set:
                    continue  # Skip neighbors that are already processed

                if tentative_g_score < g_scores[neighbor]:
                    # Found a better path to the neighbor
                    came_from[neighbor] = current
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = tentative_g_score + self.heuristics(neighbor, goal_node)
                    heapq.heappush(open_list, (f_scores[neighbor], neighbor))

        return None  # No path was found

    def reconstruct_path(self, came_from, current, total_distance):
        # Build the path from start to goal
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path, total_distance

# Example usage
nodes = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2)
]
astar = AStar(nodes)

# Add edges between nodes
astar.add_edge((0, 0), (0, 1), 1)
astar.add_edge((0, 1), (0, 2), 1)
astar.add_edge((0, 0), (1, 0), 1)
astar.add_edge((1, 0), (1, 1), 1)
astar.add_edge((1, 1), (1, 2), 1)
astar.add_edge((0, 2), (1, 2), 1)
astar.add_edge((1, 2), (2, 2), 1)
astar.add_edge((2, 2), (2, 1), 1)
astar.add_edge((2, 1), (2, 0), 1)

start_node = (0, 0)
goal_node = (2, 2)

result = astar.find_path(start_node, goal_node)

if result:
    path, distance = result
    print("Shortest path:", path)
    print("Length of the shortest path:", distance)
else:
    print("No path found.")
