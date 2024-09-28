import unittest
from algorithms.fringe_search import FringeSearchOSMnx
import networkx as nx

class TestFringeSearchOSMnx(unittest.TestCase):
    """Unit tests for the Fringe Search algorithm implemented in FringeSearchOSMnx."""

    def setUp(self):
        """Creates a simple graph for testing."""
        self.graph = nx.Graph()
        self.graph.add_edge(1, 2, length=1000.0)  # Distance in meters
        self.graph.add_edge(2, 3, length=2000.0)
        self.graph.add_edge(3, 4, length=1000.0)
        self.graph.add_edge(1, 4, length=5000.0)
        
        # Add latitude and longitude attributes for testing
        self.graph.nodes[1]['x'], self.graph.nodes[1]['y'] = 60.1699, 24.9384
        self.graph.nodes[2]['x'], self.graph.nodes[2]['y'] = 60.1700, 24.9390
        self.graph.nodes[3]['x'], self.graph.nodes[3]['y'] = 60.1710, 24.9400
        self.graph.nodes[4]['x'], self.graph.nodes[4]['y'] = 60.1720, 24.9410

        self.fringe_search = FringeSearchOSMnx(self.graph)

    def test_find_path_fringe_search(self):
        """Tests finding the shortest path using Fringe Search algorithm."""
        path, length = self.fringe_search.find_path(1, 4)
        self.assertEqual(path, [1, 2, 3, 4])
        self.assertAlmostEqual(length, 4000, delta=1)

    def test_no_path_fringe_search(self):
        """Tests that Fringe Search returns no path when the graph is disconnected."""
        self.graph.remove_edge(1, 4)
        self.graph.remove_edge(2, 3)
        path, length = self.fringe_search.find_path(1, 4)
        self.assertIsNone(path)  # Expect no path to be found

    def test_multiple_shortest_paths(self):
        """Tests the case where multiple shortest paths exist."""
        self.graph.add_edge(2, 4, length=3000.0)  # Another equally short path
        path, length = self.fringe_search.find_path(1, 4)
        self.assertIn(path, [[1, 2, 3, 4], [1, 2, 4]])
        self.assertAlmostEqual(length, 4000, delta=1)

    def test_start_node_not_in_graph(self):
        """Tests the case when the start node is not in the graph."""
        path, length = self.fringe_search.find_path(99, 4)  # Node 99 is not in the graph
        self.assertIsNone(path)

    def test_goal_node_not_in_graph(self):
        """Tests the case when the goal node is not in the graph."""
        path, length = self.fringe_search.find_path(1, 99)  # Node 99 is not in the graph
        self.assertIsNone(path)  # Expect no path to be found
    
    def test_single_node_graph(self):
        """Tests the case where the graph contains only one node."""
        graph = nx.Graph()
        graph.add_node(1, x=60.1699, y=24.9384)
        fringe_search = FringeSearchOSMnx(graph)
        path, length = fringe_search.find_path(1, 1)
        self.assertEqual(path, [1])
        self.assertAlmostEqual(length, 0.0)

    def test_cycle_in_graph(self):
        """Tests handling of a cycle in the graph."""
        self.graph.add_edge(4, 1, length=500.0)  # Create a cycle with a shorter direct path
        path, length = self.fringe_search.find_path(1, 4)
        self.assertEqual(path, [1, 4])
        self.assertAlmostEqual(length, 500, delta=1)

    def test_no_weights_on_edges(self):
        """Tests the case where some edges have no length attribute assigned."""
        self.graph.add_edge(2, 4)  # No length attribute
        path, length = self.fringe_search.find_path(1, 4)
        self.assertEqual(path, [1, 2, 3, 4])
        self.assertAlmostEqual(length, 4000.0, delta=1)


if __name__ == '__main__':
    unittest.main()
