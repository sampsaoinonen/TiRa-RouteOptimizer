from collections import deque
from utils.graph_utils import GraphUtils


class FringeSearchOSMnx:
    """Fringe Search algorithm implementation using OSMnx graph data.
    
    This class provides methods to find the shortest path between nodes in a graph 
    using the Fringe Search algorithm. It uses the Haversine distance for the 
    heuristic function to estimate the distance between geographic points.

    Attributes:
        graph (networkx.Graph): The street network graph from OSMnx.
    """
    def __init__(self, graph):
        """Initializes FringeSearchOSMnx with the provided graph.

        Args:
            graph (networkx.Graph): A NetworkX graph representing the street network.
        """
        self.graph = graph

    def find_path(self, start_node, goal_node):
        """Finds the shortest path from start_node to goal_node using the Fringe Search algorithm.

        Args:
            start_node (int): The starting node ID.
            goal_node (int): The goal node ID.

        Returns:
            tuple:
                list: The shortest path as a list of node IDs from start_node to goal_node.
                float: The total distance of the path in meters.
                If no path is found, returns (None, float('inf')).
        """
        if start_node not in self.graph.nodes or goal_node not in self.graph.nodes:
            return None, float('inf')

        # Initialize fringe and cache
        flimit = GraphUtils.haversine(self.graph, start_node, goal_node)
        cache = {start_node: (0, None)}
        fringe = deque([start_node])
        found = False

        while True:
            next_fringe = deque()
            fmin = float('inf')

            while fringe:
                current = fringe.popleft()
                g = cache[current][0]
                h = GraphUtils.haversine(self.graph, current, goal_node)
                f = g + h

                # If f exceeds the current flimit, defer this node to the next iteration
                if f > flimit:
                    if f < fmin:
                        fmin = f
                    next_fringe.append(current)
                    continue

                if current == goal_node:
                    found = True
                    break

                # Explore neighbors of the current node from right to left
                neighbors = list(self.graph.neighbors(current))
                neighbors.reverse()

                for neighbor in neighbors:
                    edge_length = GraphUtils.get_edge_length(self.graph, current, neighbor)
                    tentative_g = g + edge_length

                    if neighbor not in cache or tentative_g < cache[neighbor][0]:
                        cache[neighbor] = (tentative_g, current)

                        if neighbor in fringe:
                            fringe.remove(neighbor)

                        fringe.appendleft(neighbor)  # This ensures that it is revisited next

            if found:
                return self.reconstruct_path(cache, goal_node), cache[goal_node][0]

            if not next_fringe:
                return None, float('inf')

            fringe = next_fringe
            flimit = fmin  # Update flimit with the smallest f-value

    def reconstruct_path(self, cache, current):
        """Reconstructs the path from the start node to the current node.

        Args:
            cache (dict): A dictionary mapping nodes to their g-values and parent nodes.
            current (int): The current node ID (usually the goal node).

        Returns:
            list: The reconstructed path as a list of node IDs from the start node to the goal node.
        """
        path = [current]
        while cache[current][1] is not None:
            current = cache[current][1]
            path.append(current)
        path.reverse()
        return path
