import unittest
import random
import time
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from algorithms.a_star import AStarOSMnx
from algorithms.fringe_search import FringeSearchOSMnx

class TestAlgorithmPerformance(unittest.TestCase):
    """Performance test comparing Fringe Search and A* using the Uusimaa graph."""

    def setUp(self):
        """Downloads the OSMnx graph of Uusimaa region for performance testing."""
        print("Downloading the Uusimaa graph...")
        self.graph = ox.graph_from_place('Uusimaa, Finland', network_type='drive')
        self.a_star = AStarOSMnx(self.graph)
        self.fringe_search = FringeSearchOSMnx(self.graph)

    def test_algorithm_performance(self):
        """Runs 100 random tests comparing A* and Fringe Search and verifies correctness with Dijkstra."""
        a_star_times = []
        fringe_times = []
        distances = []

        for i in range(100):
            start_node, goal_node = self.get_random_nodes()

            print(f"\nTest {i+1}: Comparing A* and Fringe Search between nodes {start_node} and {goal_node}")

            # Perform tests for A* and Fringe Search, store results
            a_star_length, a_star_time = self.run_a_star_test(start_node, goal_node)
            fringe_length, fringe_time = self.run_fringe_search_test(start_node, goal_node)

            # Validate and log results
            self.validate_and_log_results(start_node, goal_node, a_star_length, a_star_time, fringe_length, fringe_time, a_star_times, fringe_times, distances)

        # Plotting results after all tests
        self.plot_results(distances, a_star_times, fringe_times)

    def get_random_nodes(self):
        """Returns two random, different nodes from the graph."""
        start_node = random.choice(list(self.graph.nodes))
        goal_node = random.choice(list(self.graph.nodes))
        while start_node == goal_node:
            goal_node = random.choice(list(self.graph.nodes))
        return start_node, goal_node

    def run_a_star_test(self, start_node, goal_node):
        """Runs A* algorithm test and returns path length and execution time."""
        start_time = time.time()
        path, length = self.a_star.find_path(start_node, goal_node)
        execution_time = time.time() - start_time
        return length, execution_time

    def run_fringe_search_test(self, start_node, goal_node):
        """Runs Fringe Search algorithm test and returns path length and execution time."""
        start_time = time.time()
        path, length = self.fringe_search.find_path(start_node, goal_node)
        execution_time = time.time() - start_time
        return length, execution_time

    def validate_and_log_results(self, start_node, goal_node, a_star_length, a_star_time, fringe_length, fringe_time, a_star_times, fringe_times, distances):
        """Validates results against Dijkstra and logs/prints the outcome."""
        try:
            dijkstra_length = nx.shortest_path_length(self.graph, source=start_node, target=goal_node, weight='length')
        except nx.NetworkXNoPath:
            dijkstra_length = float('inf')

        # Validate A* result
        if a_star_length is not None:
            self.assertAlmostEqual(a_star_length, dijkstra_length, delta=1)
            a_star_times.append(a_star_time)
            distances.append(a_star_length / 1000)  # Convert to kilometers
            print(f"A* found path of length {a_star_length} in {a_star_time:.4f} seconds")
        else:
            self.assertIsNone(dijkstra_length)
            a_star_times.append(float('inf'))
            print("A* found no path")

        # Validate Fringe Search result
        if fringe_length is not None:
            self.assertAlmostEqual(fringe_length, dijkstra_length, delta=1)
            fringe_times.append(fringe_time)
            print(f"Fringe Search found path of length {fringe_length} in {fringe_time:.4f} seconds")
        else:
            self.assertIsNone(dijkstra_length)
            fringe_times.append(float('inf'))
            print("Fringe Search found no path")

    def plot_results(self, distances, a_star_times, fringe_times):
        """Plots a comparison of A* and Fringe Search execution times against distances."""
        # Sort by distances to plot results in ascending order
        sorted_data = sorted(zip(distances, a_star_times, fringe_times))
        distances_sorted, a_star_times_sorted, fringe_times_sorted = zip(*sorted_data)

        plt.figure(figsize=(10, 6))
        plt.plot(distances_sorted, a_star_times_sorted, label="A* Execution Time", color='blue', marker='o', markersize=5)
        plt.plot(distances_sorted, fringe_times_sorted, label="Fringe Search Execution Time", color='red', marker='o', markersize=5)

        plt.xlabel('Distance (km)')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Execution Time Comparison: A* vs Fringe Search')
        plt.legend()
        plt.grid(True)

        # Save the plot as an image file
        plt.savefig('test-results/performance_plot.png')
        
        plt.show()


if __name__ == '__main__':
    unittest.main()
