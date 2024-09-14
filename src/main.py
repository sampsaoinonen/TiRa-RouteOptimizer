from algorithms.a_star import AStarOSMnx
from osm_utils import download_osm_graph, get_nearest_node
import osmnx as ox
import matplotlib.pyplot as plt

def main():
    """Main function to run the A* pathfinding algorithm on an OSMnx graph.

    This function downloads the OpenStreetMap graph for a specific location (Helsinki),
    finds the nearest nodes to given latitude and longitude points, runs the A* algorithm to 
    find the shortest path, and then plots and saves the path on the graph.
    """

    # Download the graph for Helsinki, Finland
    place_name = 'Helsinki, Finland'
    graph = download_osm_graph(place_name)

    # Define start and goal locations (latitude, longitude)
    start_latlng = (60.18960804900698, 24.917147255247126)  # Helsinki, Karhu Ministeri
    goal_latlng = (60.18837051116967, 24.960420722868705)  # Helsinki, Iltakoulu

    # Find the nearest graph nodes to these points
    start_node = get_nearest_node(graph, start_latlng[0], start_latlng[1])
    goal_node = get_nearest_node(graph, goal_latlng[0], goal_latlng[1])

    # Run A* algorithm
    astar = AStarOSMnx(graph)
    path, length = astar.find_path(start_node, goal_node)

    if path:
        print("Shortest path (nodes):", path)
        print(f"Path length: {length:.2f} km")

        # Plot the graph and the path
        fig, ax = ox.plot_graph_route(graph, path, route_linewidth=6, node_size=0, bgcolor='k')

        # Save the plot as an image
        filepath = 'shortest_path.png'
        fig.savefig(filepath)
        print(f"Route image saved to {filepath}")

        # Show the plot
        plt.show()
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
