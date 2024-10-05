import heapq
from utils.graph_utils import GraphUtils

class AStarOSMnx:
    """A* (A-star) algorithm implementation using OSMnx graph data.
    
    This class provides methods to find the shortest path between nodes in a graph using the
    A* algorithm. It uses the Euclidean distance for the heuristic function to estimate the
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
        """Finds the shortest path by expanding nodes based on the sum of their actual cost
        from the start node (g-score) and the estimated cost to the goal node (heuristic, h-score).
        The node with the lowest total cost (f-score = g + h) is expanded first.

        Args:
            start_node (int): The node ID where the path starts.
            goal_node (int): The node ID where the path ends.
        
        Returns:
            tuple:
                list: The shortest path as a list of node IDs, from start_node to goal_node.
                float: The total distance of the path in kilometers.
                If no path is found, returns (None, float('inf')).

        """

        if start_node not in self.graph.nodes or goal_node not in self.graph.nodes:
            return None, float('inf')

        # Initialize g-scores (cost from start) and f-scores (estimated total cost) for all nodes
        g_scores = {node: float("inf") for node in self.graph.nodes}
        g_scores[start_node] = 0

        f_scores = {node: float("inf") for node in self.graph.nodes}
        f_scores[start_node] = GraphUtils.euclidean(self.graph, start_node, goal_node)

        # Open list (priority queue) for nodes to explore and a closed set for processed nodes
        open_list = []
        heapq.heappush(open_list, (f_scores[start_node], start_node))
        closed_set = set()

        came_from = {}

        # Combine all state-related variables into one dictionary
        state = {
            'g_scores': g_scores,
            'f_scores': f_scores,
            'came_from': came_from,
            'open_list': open_list,
            'closed_set': closed_set
        }

        while state['open_list']:
            current = heapq.heappop(state['open_list'])[1]

            if current in state['closed_set']:
                continue
            state['closed_set'].add(current)

            if current == goal_node:
                reconstructed_path = self.reconstruct_path(state['came_from'], current)
                final_g_score = state['g_scores'][current]
                return reconstructed_path, final_g_score

            # Process neighbors of the current node
            self.process_neighbors(current, goal_node, state)

        return None, float("inf")

    def process_neighbors(self, current, goal_node, state):
        """Processes and evaluates the neighbors of the current node.

        Args:
            current (int): The current node being explored.
            goal_node (int): The target goal node.
            state (dict): A dictionary containing 'g_scores', 
                            'f_scores', 'came_from', 'open_list', and 'closed_set'.
        """
        g_scores = state['g_scores']
        f_scores = state['f_scores']
        came_from = state['came_from']
        open_list = state['open_list']
        closed_set = state['closed_set']

        for neighbor in self.graph.neighbors(current):
            tentative_g_score = (
                g_scores[current] + GraphUtils.get_edge_length(self.graph, current, neighbor))

            if neighbor in closed_set:
                continue

            # If a better path is found, update g-scores, f-scores, and parent mapping
            if tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = (
                    tentative_g_score + GraphUtils.euclidean(self.graph, neighbor, goal_node))
                heapq.heappush(open_list, (f_scores[neighbor], neighbor))

    def reconstruct_path(self, came_from, current):
        """Reconstructs the shortest path from the came_from dictionary.

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
        path.reverse()  # Reverse the path to get it from start to goal
        return path
