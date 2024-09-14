import unittest
from algorithms.a_star import AStarOSMnx
import networkx as nx

class TestAStarOSMnx(unittest.TestCase):

    def setUp(self):
        # Create a simple graph for testing
        self.graph = nx.Graph()
        self.graph.add_edge(1, 2, length=1000.0)
        self.graph.add_edge(2, 3, length=2000.0)
        self.graph.add_edge(3, 4, length=1000.0)
        

        # Add latitude and longitude attributes for testing
        self.graph.nodes[1]['x'], self.graph.nodes[1]['y'] = 60.1699, 24.9384
        self.graph.nodes[2]['x'], self.graph.nodes[2]['y'] = 60.1700, 24.9390
        self.graph.nodes[3]['x'], self.graph.nodes[3]['y'] = 60.1710, 24.9400
        self.graph.nodes[4]['x'], self.graph.nodes[4]['y'] = 60.1720, 24.9410

        # Initialize A* algorithm with the graph
        self.astar = AStarOSMnx(self.graph)

    def test_find_path(self):        
        path, length = self.astar.find_path(1, 4)
        self.assertEqual(path, [1, 2, 3, 4])  
        self.assertAlmostEqual(length, 4.0)

    def test_no_path(self):
        self.graph.remove_edge(2, 3)
        path, length = self.astar.find_path(1, 4)
        self.assertIsNone(path)

    
if __name__ == '__main__':
    unittest.main()
