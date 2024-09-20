import heapq
from utils.graph_utils import GraphUtils

class AStarOSMnx:
    """A* (A-star) algorithm implementation using OSMnx graph data.
    
    This class provides methods to find the shortest path between nodes in a graph using the
    A* algorithm. It uses the Haversine distance for the heuristic function to estimate the
    distance between geographic points.

    Attributes:
        graph (networkx.Graph): The street network graph from OSMnx.
    """
    def __init__(self, graph):
        """Initializes AStarOSMnx with the given graph.

        Args:
            graph (networkx.Graph): A NetworkX graph representing the street network.
        """
        self.graph = graph

    def find_path(self, start_node, goal_node):
        """ Find the shortest path using the A* algorithm.

        Args:
            start_node (int): The node ID where the path starts.
            goal_node (int): The node ID where the path ends.
        
        Returns:
            tuple:
                list: The shortest path as a list of node IDs, from start_node to goal_node.
                float: The total distance of the path in kilometers.
                If no path is found, returns (None, float('inf')).

        """

        # Check if start_node and goal_node are in the graph
        if start_node not in self.graph.nodes or goal_node not in self.graph.nodes:
            return None, float('inf')

        g_scores = {node: float("inf") for node in self.graph.nodes}
        g_scores[start_node] = 0

        f_scores = {node: float("inf") for node in self.graph.nodes}
        f_scores[start_node] = GraphUtils.haversine(self.graph, start_node, goal_node)

        open_list = []
        heapq.heappush(open_list, (f_scores[start_node], start_node))
        closed_set = set()

        came_from = {}

        while open_list:
            current = heapq.heappop(open_list)[1]

            if current in closed_set:
                continue
            closed_set.add(current)

            if current == goal_node:
                return self.reconstruct_path(came_from, current), g_scores[current]

            for neighbor in self.graph.neighbors(current):
                tentative_g_score = (g_scores[current] +
                                     GraphUtils.get_edge_length(self.graph, current, neighbor))

                if neighbor in closed_set:
                    continue

                if tentative_g_score < g_scores[neighbor]:
                    came_from[neighbor] = current
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = (tentative_g_score +
                                        GraphUtils.haversine(self.graph, neighbor, goal_node))
                    heapq.heappush(open_list, (f_scores[neighbor], neighbor))

        return None, float("inf")

    def reconstruct_path(self, came_from, current):
        """
        Reconstruct the shortest path from the came_from dictionary.

        Args:
            came_from (dict): A dictionary mapping each node to the node it came from.
            current (int): The current node ID (usually the goal node).

        Returns:
            list: The reconstructed shortest path as a list of node IDs, from start to goal.
        """
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
