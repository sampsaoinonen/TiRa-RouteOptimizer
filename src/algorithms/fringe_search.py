from utils.graph_utils import GraphUtils

class FringeSearchOSMnx:
    """ Fringe Search algorithm implementation using OSMnx graph data.
    
    This class provides methods to find the shortest path between nodes in a graph 
    using the Fringe Search algorithm. It uses the Haversine distance for the 
    heuristic function to estimate the distance between geographic points.

    Attributes:
        graph (networkx.Graph): The street network graph from OSMnx.
    """

    def __init__(self, graph):
        """ Initializes FringeSearchOSMnx with the provided graph.

        Args:
            graph (networkx.Graph): A NetworkX graph representing the street network.
        """
        self.graph = graph

    def find_path(self, start_node, goal_node):
        """ Finds the shortest path from start_node to goal_node using the Fringe Search algorithm.

        Args:
            start_node (int): The starting node ID.
            goal_node (int): The goal node ID.

        Returns:
            tuple:
                list: The shortest path as a list of node IDs from start_node to goal_node.
                float: The total distance of the path in kilometers.
                If no path is found, returns (None, float('inf')).
        """
        # Check if start_node and goal_node are in the graph
        if start_node not in self.graph.nodes or goal_node not in self.graph.nodes:
            return None, float('inf')

        # Initialize fringe and cache
        fringe = [start_node]
        cache = {start_node: (0, None)}
        flimit = GraphUtils.haversine(self.graph, start_node, goal_node)
        found = False

        while not found and fringe:
            fmin = float('inf')
            i = 0  # Index to traverse the fringe from left to right

            while i < len(fringe):
                node = fringe[i]
                g, _ = cache[node]
                h = GraphUtils.haversine(self.graph, node, goal_node)
                f = g + h

                if f > flimit:
                    fmin = min(fmin, f)
                    i += 1
                    continue

                if node == goal_node:
                    found = True
                    break

                # Expand neighbors of the current node from right to left
                neighbors = list(self.graph.neighbors(node))
                for neighbor in reversed(neighbors):
                    tentative_g = g + GraphUtils.get_edge_length(self.graph, node, neighbor)

                    if neighbor in cache and tentative_g >= cache[neighbor][0]:
                        continue

                    if neighbor in fringe:
                        fringe.remove(neighbor)

                    fringe.insert(i + 1, neighbor)
                    cache[neighbor] = (tentative_g, node)

                fringe.pop(i)

            if not found:
                if fmin == float('inf'):
                    break
                flimit = fmin  # Update flimit for the next iteration

        if found:
            path = self.reconstruct_path(cache, goal_node)
            total_length = cache[goal_node][0]
            return path, total_length

        return None, float('inf')

    def reconstruct_path(self, cache, current):
        """ Reconstructs the path from the start node to the current node.

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
