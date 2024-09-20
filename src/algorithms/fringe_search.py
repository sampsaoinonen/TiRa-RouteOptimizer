import math

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

    def haversine(self, node1, node2):
        """ Calculates the Haversine distance between two geographic points.
        https://rosettacode.org/wiki/Haversine_formula
        
        Args:
            node1 (int): The first node ID.
            node2 (int): The second node ID.

        Returns:
            float: The distance between the two points in kilometers.
        """
        lat1 = self.graph.nodes[node1]['y']
        lon1 = self.graph.nodes[node1]['x']
        lat2 = self.graph.nodes[node2]['y']
        lon2 = self.graph.nodes[node2]['x']
        r = 6371.0  # Earth's radius in kilometers
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)
        a = math.sin(dLat / 2) ** 2 + \
            math.cos(lat1) * math.cos(lat2) * math.sin(dLon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        return r * c

    def get_edge_length(self, current, neighbor):
        """ Gets the length of the edge between current and neighbor in kilometers.
        
        Args:
            current (int): Current node ID.
            neighbor (int): Neighbor node ID.
        
        Returns:
            float: Edge length in kilometers (converted from meters if needed).
        """
        edge_data = self.graph.get_edge_data(current, neighbor)
        
        if isinstance(edge_data, dict):
            if 'length' in edge_data:
                return edge_data['length'] / 1000.0  # Convert meters to kilometers
        # Handle OSMnx multi-edge graphs (parallel edges)
            if 0 in edge_data:
                return edge_data[0].get('length', 0) / 1000.0 
        return 0.0  # Default to 0 if no length is found

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
        # Initialize fringe and cache
        fringe = [start_node]  
        cache = {start_node: (0, None)}
        flimit = self.haversine(start_node, goal_node)
        found = False

        while not found and fringe:
            fmin = float('inf')
            i = 0  # Index to traverse the fringe from left to right

            while i < len(fringe):
                node = fringe[i]
                g, parent = cache[node]
                h = self.haversine(node, goal_node)
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
                    tentative_g = g + self.get_edge_length(node, neighbor)

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
        else:
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
