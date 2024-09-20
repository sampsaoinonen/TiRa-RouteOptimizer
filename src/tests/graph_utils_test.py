import unittest
import math
import networkx as nx
from utils.graph_utils import GraphUtils

class TestGraphUtils(unittest.TestCase):

    def setUp(self):
        # Create a simple graph for testing
        self.graph = nx.Graph()
        # Add edges with lengths in meters
        self.graph.add_edge(1, 2, length=1000.0)  # 1000 meters
        self.graph.add_edge(2, 3, length=2000.0)  # 2000 meters
        self.graph.add_edge(3, 4, length=1500.0)  # 1500 meters

        # Add latitude and longitude attributes for nodes
        # Helsinki coordinates for simplicity
        self.graph.nodes[1]['y'], self.graph.nodes[1]['x'] = 60.1699, 24.9384  # Node 1
        self.graph.nodes[2]['y'], self.graph.nodes[2]['x'] = 60.1700, 24.9390  # Node 2
        self.graph.nodes[3]['y'], self.graph.nodes[3]['x'] = 60.1705, 24.9395  # Node 3
        self.graph.nodes[4]['y'], self.graph.nodes[4]['x'] = 60.1710, 24.9400  # Node 4

    def test_get_edge_length(self):
        # Test the get_edge_length function between Node 1 and Node 2
        edge_length = GraphUtils.get_edge_length(self.graph, 1, 2)
        expected_length = 1.0  # Length in kilometers (1000 meters / 1000)
        self.assertEqual(edge_length, expected_length)

    def test_get_edge_length_no_edge(self):
        # Test get_edge_length between nodes with no direct edge
        edge_length = GraphUtils.get_edge_length(self.graph, 1, 3)
        expected_length = 0.0  # No edge between Node 1 and Node 3
        self.assertEqual(edge_length, expected_length)

    def test_get_edge_length_multi_edge(self):
        # If the graph has multi-edges, ensure the length is retrieved correctly
        # For this test, we'll add multiple edges between two nodes
        self.graph = nx.MultiGraph()  # Use MultiGraph to allow parallel edges
        self.graph.add_edge(1, 2, key=0, length=1000.0)
        self.graph.add_edge(1, 2, key=1, length=1500.0)
        edge_length = GraphUtils.get_edge_length(self.graph, 1, 2)
        expected_length = 1.0  # Should return the length of the first edge (1000 meters / 1000)
        self.assertEqual(edge_length, expected_length)

    def test_haversine(self):
        # Test the Haversine distance between two nodes
        distance = GraphUtils.haversine(self.graph, 1, 2)
        expected_distance = 0.035  # Updated expected distance in kilometers
        self.assertAlmostEqual(distance, expected_distance, places=3)

    def test_euclidean(self):
        # Test the Euclidean distance between two nodes
        distance = GraphUtils.euclidean(self.graph, 1, 2)
        expected_distance = math.sqrt((24.9390 - 24.9384) ** 2 + (60.1700 - 60.1699) ** 2)
        self.assertAlmostEqual(distance, expected_distance, places=6)

    def test_manhattan(self):
        # Test the Manhattan distance between two nodes
        distance = GraphUtils.manhattan(self.graph, 1, 2)
        expected_distance = abs(24.9390 - 24.9384) + abs(60.1700 - 60.1699)
        self.assertAlmostEqual(distance, expected_distance, places=6)

if __name__ == '__main__':
    unittest.main()
