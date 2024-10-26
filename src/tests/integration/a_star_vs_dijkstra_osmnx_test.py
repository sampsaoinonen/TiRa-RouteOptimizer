import unittest
import random
import osmnx as ox
import networkx as nx
from algorithms.a_star import AStarOSMnx

class TestAStarVsDijkstraOSMnx(unittest.TestCase):
    """Integration tests to compare A* and Dijkstra algorithms using OSMnx data."""

    def setUp(self):
        """Downloads the OSMnx graph for Helsinki, Finland and sets a random seed."""
        self.graph = ox.graph_from_place('Helsinki, Finland', network_type='drive')
        self.astar = AStarOSMnx(self.graph)
        random.seed(42)  # Set seed for reproducibility

    def test_compare_astar_dijkstra_osmnx(self):
        """Compare A* and Dijkstra algorithms with random start and goal nodes from OSMnx graph."""
        print("")
        print("_____")

        # Define the number of random tests to perform
        for i in range(10):
            # Randomly select start and goal nodes
            start_node = random.choice(list(self.graph.nodes))
            goal_node = random.choice(list(self.graph.nodes))

            # Ensure start and goal nodes are different
            while start_node == goal_node:
                goal_node = random.choice(list(self.graph.nodes))

            # Print the nodes being tested
            print(f"Test {i+1}: Start node = {start_node}, Goal node = {goal_node}")

            # Test A* algorithm
            a_star_path, a_star_length = self.astar.find_path(start_node, goal_node)
            print(f"A* path length: {a_star_length if a_star_path else 'No path found'}")

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
            if a_star_path:
                try:
                    self.assertAlmostEqual(a_star_length, dijkstra_length, delta=1)
                    print("Test passed: Path lengths match.")
                except AssertionError as e:
                    print(f"Test failed: Path lengths do not match. A*: {a_star_length}, Dijkstra: {dijkstra_length}")
                    raise e
            else:
                print(f"A* did not find a path between {start_node} and {goal_node}")
                self.fail(f"A* did not find a path between {start_node} and {goal_node}")
            print("_____")

if __name__ == '__main__':
    unittest.main()
