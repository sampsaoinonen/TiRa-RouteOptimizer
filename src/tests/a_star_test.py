import unittest
from algorithms.a_star import AStarOSMnx
import networkx as nx
import random

class TestAStarOSMnx(unittest.TestCase):

    def setUp(self):
        # Create a simple graph for testing
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

        # Initialize A* algorithm with the graph
        self.astar = AStarOSMnx(self.graph)

    def test_find_path_astar(self):
        # Test finding the shortest path using A* algorithm
        path, length = self.astar.find_path(1, 4)
        self.assertEqual(path, [1, 2, 3, 4])  # The shortest path is 1 -> 2 -> 3 -> 4
        self.assertAlmostEqual(length, 4.0, delta=0.01)

    def test_no_path_astar(self):
        # Remove edges to make the graph disconnected
        self.graph.remove_edge(1, 4)
        self.graph.remove_edge(2, 3)
        path, length = self.astar.find_path(1, 4)
        self.assertIsNone(path)

    def test_multiple_shortest_paths(self):
        # Test the case where multiple shortest paths exist
        self.graph.add_edge(2, 4, length=3000.0)  # Another equally short path
        path, length = self.astar.find_path(1, 4)
        self.assertIn(path, [[1, 2, 3, 4], [1, 2, 4]])
        self.assertAlmostEqual(length, 4.0, delta=0.01)

    def test_compare_astar_dijkstra(self):
        # Run A* and Dijkstra algorithms 10 times with random start and goal nodes
        for _ in range(10):
            # Randomly select start and goal nodes from the graph
            start_node = random.choice(list(self.graph.nodes))
            goal_node = random.choice(list(self.graph.nodes))
            
            # Ensure start and goal are different
            while start_node == goal_node:
                goal_node = random.choice(list(self.graph.nodes))

            # Test A* algorithm
            a_star_path, a_star_length = self.astar.find_path(start_node, goal_node)

            # Test Dijkstra algorithm using NetworkX            
            dijkstra_length = nx.shortest_path_length(self.graph, source=start_node, target=goal_node, weight='length') / 1000.0  # Convert to km

            # Assert both algorithms return the same path length
            if a_star_path:
                self.assertAlmostEqual(a_star_length, dijkstra_length, delta=0.01)
            else:
                self.assertIsNone(a_star_path)

    def test_start_node_not_in_graph(self):
        # Test when start node is not in the graph
        path, length = self.astar.find_path(99, 4)  # Node 99 is not in the graph
        self.assertIsNone(path)  # Expect no path to be found

    def test_goal_node_not_in_graph(self):
        # Test when goal node is not in the graph
        path, length = self.astar.find_path(1, 99)  # Node 99 is not in the graph
        self.assertIsNone(path)  # Expect no path to be found

    def test_single_node_graph(self):
        # Test the case where the graph contains only one node
        graph = nx.Graph()
        graph.add_node(1, x=60.1699, y=24.9384)
        astar = AStarOSMnx(graph)
        path, length = astar.find_path(1, 1)
        self.assertEqual(path, [1])
        self.assertAlmostEqual(length, 0.0)

    def test_cycle_in_graph(self):
        # Test handling of a cycle in the graph
        self.graph.add_edge(4, 1, length=500.0)  # Create a cycle with a shorter direct path
        path, length = self.astar.find_path(1, 4)
        
        # Expect the algorithm to take the shorter path [1, 4]
        self.assertEqual(path, [1, 4])
        self.assertAlmostEqual(length, 0.5, delta=0.01)  # Total length is 500 meters (0.5 km)

    def test_no_weights_on_edges(self):
        # Test the case where some edges have no weight assigned
        self.graph.add_edge(2, 4)  # No length assigned
        path, length = self.astar.find_path(1, 4)
        self.assertEqual(path, [1, 2, 4])

if __name__ == '__main__':
    unittest.main()
