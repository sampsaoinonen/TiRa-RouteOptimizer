import heapq
import math

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
    
    def haversine(self, lat1, lon1, lat2, lon2):
        """
        Calculates the Haversine distance between two geographic points.
        https://rosettacode.org/wiki/Haversine_formula
        
        Args:
            lat1 (float): Latitude of the first point.
            lon1 (float): Longitude of the first point.
            lat2 (float): Latitude of the second point.
            lon2 (float): Longitude of the second point.

        Returns:
            float: The distance between the two points in kilometers.
        """
        r = 6372.8  # Earth's radius in kilometers
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)
        a = math.sin(dLat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dLon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        return r * c

    def find_path(self, start_node, goal_node):
        """
        Find the shortest path using the A* algorithm.

        Args:
            start_node (int): The node ID where the path starts.
            goal_node (int): The node ID where the path ends.
        
        Returns:
            tuple:
                list: The shortest path as a list of node IDs, from start_node to goal_node.
                float: The total distance of the path in kilometers.
                If no path is found, returns (None, float('inf')).

        """
        g_scores = {node: float("inf") for node in self.graph.nodes}
        g_scores[start_node] = 0

        f_scores = {node: float("inf") for node in self.graph.nodes}
        f_scores[start_node] = self.haversine(self.graph.nodes[start_node]['y'], self.graph.nodes[start_node]['x'], 
                                              self.graph.nodes[goal_node]['y'], self.graph.nodes[goal_node]['x'])

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
                edge_length = self.graph.get_edge_data(current, neighbor).get('length', 0)  # Default to 0 if 'length' is missing
                tentative_g_score = g_scores[current] + edge_length / 1000.0  # Convert meters to km
                
                if neighbor in closed_set:
                    continue

                if tentative_g_score < g_scores[neighbor]:
                    came_from[neighbor] = current
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = tentative_g_score + self.haversine(self.graph.nodes[neighbor]['y'], self.graph.nodes[neighbor]['x'], 
                                                                            self.graph.nodes[goal_node]['y'], self.graph.nodes[goal_node]['x'])
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
