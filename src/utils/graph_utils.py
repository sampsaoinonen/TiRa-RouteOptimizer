import math

class GraphUtils:
    @staticmethod
    def haversine(graph, node1, node2):
        """ Calculates the Haversine distance between two geographic points.
        https://rosettacode.org/wiki/Haversine_formula
        
        Args:
            lat1 (float): Latitude of the first point.
            lon1 (float): Longitude of the first point.
            lat2 (float): Latitude of the second point.
            lon2 (float): Longitude of the second point.

        Returns:
            float: The distance between the two points in kilometers.
        """
        lat1 = graph.nodes[node1]['y']
        lon1 = graph.nodes[node1]['x']
        lat2 = graph.nodes[node2]['y']
        lon2 = graph.nodes[node2]['x']
        r = 6371  # Earth's radius in kilometers
        d_lat = math.radians(lat2 - lat1)
        d_lon = math.radians(lon2 - lon1)
        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)
        a = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        return r * c

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
    def manhattan(graph, node1, node2):
        """ Calculates the Manhattan distance between two points.
        
        Args:
            node1 (int): ID of the first node.
            node2 (int): ID of the second node.

        Returns:
            float: The Manhattan distance between the two points.
        """
        x1 = graph.nodes[node1]['x']
        y1 = graph.nodes[node1]['y']
        x2 = graph.nodes[node2]['x']
        y2 = graph.nodes[node2]['y']

        # Manhattan distance formula
        distance = abs(x2 - x1) + abs(y2 - y1)
        return distance


    @staticmethod
    def get_edge_length(graph, current, neighbor):
        """ Gets the length of the edge between current and neighbor in kilometers.
        
        Args:
            current (int): Current node ID.
            neighbor (int): Neighbor node ID.
        
        Returns:
            float: Edge length in kilometers (converted from meters if needed).
        """
        edge_data = graph.get_edge_data(current, neighbor)

        if isinstance(edge_data, dict):
            if 'length' in edge_data:
                return edge_data['length'] / 1000.0  # Convert meters to kilometers
            # Handle OSMnx multi-edge graphs (parallel edges)
            if 0 in edge_data:
                return edge_data[0].get('length', 0) / 1000.0
        return 0.0  # Default to 0 if no length is found
