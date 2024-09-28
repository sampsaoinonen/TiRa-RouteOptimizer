import unittest
import osmnx as ox
import networkx as nx
import random
from algorithms.fringe_search import FringeSearchOSMnx

class TestFringeSearchVsDijkstraOSMnx(unittest.TestCase):
    """Integration tests to compare Fringe Search and Dijkstra algorithms using OSMnx data."""

    def setUp(self):
        """Set up the OSMnx graph and initialize the algorithms."""
        self.graph = ox.graph_from_place('Helsinki, Finland', network_type='drive')
        self.fringe_search = FringeSearchOSMnx(self.graph)
        random.seed(42)  # Set seed for reproducibility

    def test_compare_fringe_dijkstra_osmnx(self):
        """Compare Fringe Search and Dijkstra algorithms with random start and goal nodes."""
        for _ in range(10):
            # Randomly select start and goal nodes
            start_node = random.choice(list(self.graph.nodes))
            goal_node = random.choice(list(self.graph.nodes))

            # Ensure start and goal nodes are different
            while start_node == goal_node:
                goal_node = random.choice(list(self.graph.nodes))

            # Test Fringe Search algorithm
            fringe_path, fringe_length = self.fringe_search.find_path(start_node, goal_node)

            # Test Dijkstra algorithm using NetworkX
            try:
                dijkstra_length = nx.shortest_path_length(
                    self.graph, source=start_node, target=goal_node, weight='length'
                )
            except nx.NetworkXNoPath:
                # If Dijkstra can't find a path, skip this iteration
                continue

            # Assert both algorithms return the same path length
            if fringe_path:
                self.assertAlmostEqual(fringe_length, dijkstra_length, delta=1)
            else:
                self.fail(f"Fringe Search did not find a path between {start_node} and {goal_node}")

if __name__ == '__main__':
    unittest.main()
