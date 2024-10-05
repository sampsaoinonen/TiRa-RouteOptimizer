from collections import deque
from utils.graph_utils import GraphUtils


class FringeSearchOSMnx:
    """Fringe Search algorithm implementation using OSMnx graph data.
    
    This class provides methods to find the shortest path between nodes in a graph 
    using the Fringe Search algorithm. It uses the Euclidean distance for the 
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
        """Finds the shortest path using the Fringe Search algorithm.

        The algorithm explores nodes by evaluating the combined cost (f-value) 
        of the distance from the start node (g-value) and the estimated distance 
        to the goal node (h-value).
        
        - g-value: The actual cost from the start node to the current node.
        - h-value: The heuristic estimate of the remaining cost from the current node to the goal.
        - f-value: The sum of g-value and h-value (f = g + h), representing the estimated total cost.

        Nodes with an f-value above a threshold (flimit) are deferred to a future iteration.

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

        # Initialize the first threshold (flimit) using the heuristic from the start to the goal
        flimit = GraphUtils.euclidean(self.graph, start_node, goal_node)

        # Cache stores g-values (actual cost from start) and parent of each visited node
        cache = {start_node: (0, None)}

        # Initialize the fringe (queue) with the start node
        fringe = deque([start_node])
        found = False

        while True:
            # Process nodes in the fringe
            next_fringe, fmin, found = self.process_fringe(fringe, goal_node, flimit, cache)

            if found:
                return self.reconstruct_path(cache, goal_node), cache[goal_node][0]

            if not next_fringe:
                return None, float('inf')

            # Move to the next iteration with updated fringe and flimit
            fringe = next_fringe
            flimit = fmin

    def process_fringe(self, fringe, goal_node, flimit, cache):
        """Processes nodes in the fringe, expanding and evaluating neighbors.

        This method evaluates nodes in the current fringe and updates their 
        f-values. Nodes exceeding the flimit are deferred to a future iteration.

        Args:
            fringe (deque): The queue of nodes to explore.
            goal_node (int): The goal node ID.
            flimit (float): The current f-value limit.
            cache (dict): A dictionary storing g-values and parent nodes.

        Returns:
            tuple: The updated fringe for the next iteration, the minimum f-value, 
            and a boolean indicating if the goal node was found.
        """
        next_fringe = deque()
        fmin = float('inf')
        found = False

        while fringe:
            current = fringe.popleft()
            g = cache[current][0]
            h = GraphUtils.euclidean(self.graph, current, goal_node)
            f = g + h

            if f > flimit:
                fmin = min(fmin, f)
                next_fringe.append(current)
                continue

            if current == goal_node:
                found = True
                break

            # Expand neighbors of the current node
            self.expand_neighbors(current, fringe, cache)

        return next_fringe, fmin, found

    def expand_neighbors(self, current, fringe, cache):
        """Expands and processes neighbors of the current node.

        This method explores the neighboring nodes of the current node, 
        calculates their tentative g-values, and updates the cache and fringe.

        Args:
            current (int): The current node being explored.
            fringe (deque): The queue of nodes to explore.
            cache (dict): A dictionary storing g-values and parent nodes.
        """
        neighbors = list(self.graph.neighbors(current))
        neighbors.reverse()

        for neighbor in neighbors:
            edge_length = GraphUtils.get_edge_length(self.graph, current, neighbor)
            tentative_g = cache[current][0] + edge_length

            if neighbor not in cache or tentative_g < cache[neighbor][0]:
                cache[neighbor] = (tentative_g, current)

                if neighbor in fringe:
                    fringe.remove(neighbor)

                # Add the neighbor to the front of the fringe
                fringe.appendleft(neighbor)

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
        path.reverse() # Reverse the list to get the path from start to goal
        return path
