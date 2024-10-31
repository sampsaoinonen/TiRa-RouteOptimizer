import unittest
import osmnx as ox
import networkx as nx
import random
from algorithms.fringe_search import FringeSearchOSMnx

class TestFringeSearchVsDijkstraOSMnx(unittest.TestCase):
    """Integration tests to compare Fringe Search and Dijkstra algorithms using OSMnx data."""

    def setUp(self):
        """Downloads the OSMnx graph for Helsinki, Finland."""
        self.graph = ox.graph_from_place('Helsinki, Finland', network_type='drive')
        self.fringe_search = FringeSearchOSMnx(self.graph)

    def test_compare_fringe_dijkstra_osmnx(self):
        """Compare Fringe Search and Dijkstra algorithms with random start and goal nodes from OSMnx graph."""
        print("")
        print("_____")

        for i in range(10):
            # Randomly select start and goal nodes
            start_node = random.choice(list(self.graph.nodes))
            goal_node = random.choice(list(self.graph.nodes))

            # Ensure start and goal nodes are different
            while start_node == goal_node:
                goal_node = random.choice(list(self.graph.nodes))

            # Print the nodes being tested
            print(f"Test {i+1}: Start node = {start_node}, Goal node = {goal_node}")

            # Test Fringe Search algorithm
            fringe_path, fringe_length = self.fringe_search.find_path(start_node, goal_node)
            print(f"Fringe Search path length: {fringe_length if fringe_path else 'No path found'}")

            # Test Dijkstra algorithm using NetworkX
            try:
                dijkstra_length = nx.shortest_path_length(
                    self.graph, source=start_node, target=goal_node, weight='length'
                )
                print(f"Dijkstra path length: {dijkstra_length}")
            except nx.NetworkXNoPath:
                # If Dijkstra can't find a path, skip this iteration
                print("Dijkstra did not find a path.")
                continue

            # Assert both algorithms return the same path length
            if fringe_path:
                try:
                    self.assertAlmostEqual(fringe_length, dijkstra_length, delta=1)
                    print("Test passed: Path lengths match.")
                except AssertionError as e:
                    print(f"Test failed: Path lengths do not match. Fringe: {fringe_length}, Dijkstra: {dijkstra_length}")
                    raise e
            else:
                print(f"Fringe Search did not find a path between {start_node} and {goal_node}")
                self.fail(f"Fringe Search did not find a path between {start_node} and {goal_node}")
            print("_____")


if __name__ == '__main__':
    unittest.main()
