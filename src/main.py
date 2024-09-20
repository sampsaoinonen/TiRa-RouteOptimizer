import time
import random
import osmnx as ox
import matplotlib.pyplot as plt
from algorithms.a_star import AStarOSMnx
from algorithms.fringe_search import FringeSearchOSMnx
from utils.osm_utils import download_osm_graph, get_nearest_node



def run_algorithm(algorithm_class, graph, start_node, goal_node, algorithm_name):
    """Run the specified pathfinding algorithm and return the results.

    Args:
        algorithm_class (class): The class implementing the pathfinding algorithm.
        graph (networkx.Graph): The graph to search.
        start_node (int): The starting node ID.
        goal_node (int): The goal node ID.
        algorithm_name (str): The name of the algorithm (for display purposes).

    Returns:
        tuple: A tuple containing the path (list of node IDs)
        , path length (float), and execution time (float).
    """
    print(f"Running {algorithm_name} algorithm...")
    start_time = time.time()
    algorithm = algorithm_class(graph)
    path, length = algorithm.find_path(start_node, goal_node)
    end_time = time.time()
    total_time = end_time - start_time

    if path:
        print(f"{algorithm_name} Shortest path (nodes): {path}")
        print(f"{algorithm_name} Path length: {length:.2f} km")
        print(f"{algorithm_name} Algorithm took {total_time:.4f} seconds to complete.")
        print()
        print("Close the map window to continue.")
        print()

        # Plot the graph and the path
        fig, _ = ox.plot_graph_route(
            graph, path, route_linewidth=6, node_size=0, bgcolor='k'
        )

        # Save the path as an image
        filepath = f"shortest_path_{algorithm_name.lower().replace(' ', '_')}.png"
        fig.savefig(filepath)
        print(f"{algorithm_name} Route image saved to {filepath}")

        # Show the path plot
        plt.show()
    else:
        print(f"{algorithm_name} did not find a path.")

    return path, total_time


def compare_paths_and_times(path_a, time_a, path_b, time_b):
    """Compare the paths and execution times of two algorithms.

    Args:
        path_a (list): Path returned by the first algorithm.
        time_a (float): Execution time of the first algorithm.
        name_a (str): Name of the first algorithm.
        path_b (list): Path returned by the second algorithm.
        time_b (float): Execution time of the second algorithm.
        name_b (str): Name of the second algorithm.
    """
    # Compare the two paths
    if path_a == path_b:
        print("A* and Fringe Search returned the SAME path.")
    else:
        print("A* and Fringe Search returned DIFFERENT paths.")

    # Compare execution times
    if time_a < time_b:
        time_diff = time_b - time_a
        print(f"\nA* was faster by {time_diff:.4f} seconds.")
    elif time_b < time_a:
        time_diff = time_a - time_b
        print(f"\nFringe Search was faster by {time_diff:.4f} seconds.")
    else:
        print("\nBoth algorithms took the same amount of time.")

def get_random_node(graph):
    """Get a random node from the graph."""
    return random.choice(list(graph.nodes))


def main():
    """Main function to run both A* and Fringe Search pathfinding algorithms on an OSMnx graph.

    This function downloads the OpenStreetMap graph for a specific location (Helsinki),
    finds the nearest nodes to given latitude and longitude points, runs both A* and Fringe Search
    algorithms to find the shortest paths, and then plots and saves the paths on the graph.
    """
    # Introduction
    print()
    print("Welcome to the A* and Fringe Search pathfinding algorithm comparison!")
    print("This program will find the shortest path between two points on the Helsinki map.")
    print()
    print("First let's download the OSMnx graph for Helsinki, Finland. Please wait...")
    print()

    # Download the graph for Helsinki, Finland
    place_name = 'Helsinki, Finland'
    graph = download_osm_graph(place_name)

    # Get user choice
    print("Choose an option:")
    print("1. Use predefined start and goal points (Lauttasaari -> Puroniityntie).")
    print("2. Use random start and goal points in Helsinki.")
    print("3. Input your own points for start and goal coordinates. "
    "(if coordinates are not in Helsinki,")
    print("   the program will find the nearest nodes)")
    print()

    choice = input("Enter your choice (1, 2, 3): ")

    if choice == "1":
        # Predefined start and goal locations (Helsinki, Lauttasaari -> Helsinki, Puroniityntie)
        start_latlng = (60.14758, 24.88784)  # Helsinki, Lauttasaari
        goal_latlng = (60.28333, 25.23891)   # Helsinki, Puroniityntie
        start_node = get_nearest_node(graph, start_latlng[0], start_latlng[1])
        goal_node = get_nearest_node(graph, goal_latlng[0], goal_latlng[1])
    elif choice == "2":
        # Random start and goal nodes
        start_node = get_random_node(graph)
        goal_node = get_random_node(graph)
        while start_node == goal_node:
            goal_node = get_random_node(graph)
        print(f"Random start node: {start_node}, Random goal node: {goal_node}")
    elif choice == "3":
        # User inputs coordinates
        start_lat = float(input("Enter the latitude of the start point: "))
        start_lon = float(input("Enter the longitude of the start point: "))
        goal_lat = float(input("Enter the latitude of the goal point: "))
        goal_lon = float(input("Enter the longitude of the goal point: "))
        start_node = get_nearest_node(graph, start_lat, start_lon)
        goal_node = get_nearest_node(graph, goal_lat, goal_lon)
    else:
        print("Invalid choice. Exiting.")
        return

    # Run A* algorithm
    path_a_star, astar_time = run_algorithm(
        AStarOSMnx, graph, start_node, goal_node, "A*"
    )

    # Run Fringe Search algorithm
    path_fringe, fringe_time = run_algorithm(
        FringeSearchOSMnx, graph, start_node, goal_node, "Fringe Search"
    )

    # Compare the two paths and execution times
    compare_paths_and_times(path_a_star, astar_time, path_fringe, fringe_time)


if __name__ == "__main__":
    main()
