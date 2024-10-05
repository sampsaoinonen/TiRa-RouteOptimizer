import math

class GraphUtils:
    @staticmethod
    def euclidean(graph, node1, node2):
        """ Calculates the Euclidean distance between two points.
        
        Args:
            node1 (int): ID of the first node.
            node2 (int): ID of the second node.

        Returns:
            float: The Euclidean distance between the two points.
        """
        x1 = graph.nodes[node1]['x']
        y1 = graph.nodes[node1]['y']
        x2 = graph.nodes[node2]['x']
        y2 = graph.nodes[node2]['y']

        # Euclidean distance formula
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    @staticmethod
    def get_edge_length(graph, node1, node2):
        """Fetches the length of the edge between two nodes in a graph.
        
        Args:
            graph (networkx.Graph or networkx.MultiGraph): The graph containing the edge.
            node1 (int): The starting node ID.
            node2 (int): The ending node ID.
        
        Returns:
            float: The length of the edge if available, otherwise float('inf').
        """
        edge_data = graph.get_edge_data(node1, node2)

        if edge_data:
            if graph.is_multigraph():
                # If graph is MultiGraph, find the edge with the minimum length
                return min(
                    (data.get('length', float('inf')) for key, data in edge_data.items()),
                    default=float('inf')
                )
            # Single Graph case, check if 'length' attribute exists
            return edge_data.get('length', float('inf'))

        # No valid edge exists
        return float('inf')
