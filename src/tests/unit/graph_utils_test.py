import unittest
import math
import networkx as nx
from utils.graph_utils import GraphUtils

class TestGraphUtils(unittest.TestCase):
    """Unit tests for the GraphUtils class, testing edge length retrieval and distance calculations."""

    def setUp(self):
        """Sets up a simple graph for testing with edges and geographic coordinates."""
        self.graph = nx.Graph()
        self.graph.add_edge(1, 2, length=1000.0)  # 1000 meters
        self.graph.add_edge(2, 3, length=2000.0)
        self.graph.add_edge(3, 4, length=1500.0)  # 1500 meters

        # Add latitude and longitude attributes for nodes (Helsinki coordinates)
        self.graph.nodes[1]['y'], self.graph.nodes[1]['x'] = 60.1699, 24.9384
        self.graph.nodes[2]['y'], self.graph.nodes[2]['x'] = 60.1700, 24.9390
        self.graph.nodes[3]['y'], self.graph.nodes[3]['x'] = 60.1705, 24.9395
        self.graph.nodes[4]['y'], self.graph.nodes[4]['x'] = 60.1710, 24.9400

    def test_get_edge_length(self):
        """Tests retrieving the length of an edge between two nodes."""
        edge_length = GraphUtils.get_edge_length(self.graph, 1, 2)
        self.assertEqual(edge_length, 1000.0)

    def test_get_edge_length_no_edge(self):
        """Tests that retrieving the length of a non-existing edge returns infinity."""
        edge_length = GraphUtils.get_edge_length(self.graph, 1, 3)
        self.assertEqual(edge_length, float('inf'))

    def test_get_edge_length_multi_edge(self):
        """Tests retrieving the minimum edge length in a MultiGraph with multiple parallel edges."""
        self.graph = nx.MultiGraph()  # Use MultiGraph to allow parallel edges
        self.graph.add_edge(1, 2, key=0, length=1000.0)
        self.graph.add_edge(1, 2, key=1, length=1500.0)
        edge_length = GraphUtils.get_edge_length(self.graph, 1, 2)
        self.assertEqual(edge_length, 1000)

    def test_euclidean(self):
        """Tests calculating the Euclidean distance between two nodes."""
        distance = GraphUtils.euclidean(self.graph, 1, 2)
        expected_distance = math.sqrt((24.9390 - 24.9384) ** 2 + (60.1700 - 60.1699) ** 2)
        self.assertAlmostEqual(distance, expected_distance, places=6)

if __name__ == '__main__':
    unittest.main()
