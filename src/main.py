from algorithms.a_star import AStarOSMnx
from algorithms.fringe_search import FringeSearchOSMnx
from utils.osm_utils import download_osm_graph, get_nearest_node
import osmnx as ox
import matplotlib.pyplot as plt
import time

def main():
    """ Main function to run both A* and Fringe Search pathfinding algorithms on an OSMnx graph.

    This function downloads the OpenStreetMap graph for a specific location (Helsinki),
    finds the nearest nodes to given latitude and longitude points, runs both A* and Fringe Search
    algorithms to find the shortest paths, and then plots and saves the paths on the graph.
    """

    # Download the graph for Helsinki, Finland
    place_name = 'Helsinki, Finland'
    graph = download_osm_graph(place_name)

    # Define start and goal locations (latitude, longitude)
    start_latlng = (60.14758, 24.88784)  # Helsinki, Lauttasaari
    goal_latlng = (60.28333, 25.23891)  # Helsinki, Puroniityntie

    # Find the nearest graph nodes to these points
    start_node = get_nearest_node(graph, start_latlng[0], start_latlng[1])
    goal_node = get_nearest_node(graph, goal_latlng[0], goal_latlng[1])

    # Run A* algorithm
    print("Running A* algorithm...")
    start_time = time.time()
    astar = AStarOSMnx(graph)
    path_a_star, length_a_star = astar.find_path(start_node, goal_node)
    end_time = time.time()
    astar_time = end_time - start_time

    if path_a_star:
        print("A* Shortest path (nodes):", path_a_star)
        print(f"A* Path length: {length_a_star:.2f} km")
        print(f"A* Algorithm took {astar_time:.4f} seconds to complete.")

        # Plot the graph and the A* path
        fig, ax = ox.plot_graph_route(graph, path_a_star, route_linewidth=6, node_size=0, bgcolor='k')

        # Save the A* path as an image
        filepath_a_star = 'shortest_path_a_star.png'
        fig.savefig(filepath_a_star)
        print(f"A* Route image saved to {filepath_a_star}")

        # Show the A* path plot
        plt.show()
    else:
        print("A* did not find a path.")

    # Run Fringe Search algorithm
    print("\nRunning Fringe Search algorithm...")
    start_time = time.time()
    fringe_search = FringeSearchOSMnx(graph)
    path_fringe, length_fringe = fringe_search.find_path(start_node, goal_node)
    end_time = time.time()
    fringe_time = end_time - start_time

    if path_fringe:
        print("Fringe Search Shortest path (nodes):", path_fringe)
        print(f"Fringe Search Path length: {length_fringe:.2f} km")
        print(f"Fringe Search Algorithm took {fringe_time:.4f} seconds to complete.")

        # Plot the graph and the Fringe Search path
        fig, ax = ox.plot_graph_route(graph, path_fringe, route_linewidth=6, node_size=0, bgcolor='k')

        # Save the Fringe Search path as an image
        filepath_fringe = 'shortest_path_fringe_search.png'
        fig.savefig(filepath_fringe)
        print(f"Fringe Search Route image saved to {filepath_fringe}")

        # Show the Fringe Search path plot
        plt.show()
    else:
        print("Fringe Search did not find a path.")

    # Compare the two paths and print whether they are the same
    if path_a_star == path_fringe:
        print("\nA* and Fringe Search returned the SAME path.")
    else:
        print("\nA* and Fringe Search returned DIFFERENT paths.")

    # Compare execution times and print which algorithm was faster
    if astar_time < fringe_time:
        time_diff = fringe_time - astar_time
        print(f"\nA* was faster by {time_diff:.4f} seconds.")
    elif fringe_time < astar_time:
        time_diff = astar_time - fringe_time
        print(f"\nFringe Search was faster by {time_diff:.4f} seconds.")
    else:
        print("\nBoth algorithms took the same amount of time.")


if __name__ == "__main__":
    main()
