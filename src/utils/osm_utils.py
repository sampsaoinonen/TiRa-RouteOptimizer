import osmnx as ox

def download_osm_graph(place_name, network_type='drive'):
    """ Downloads the OSMnx graph for the specified location.

    Args:
        place_name (str): Name of the place to download the graph for (e.g., 'Helsinki, Finland')
        network_type (str): The type of network to download (e.g., 'drive' for car-accessible roads)
                            Defaults to 'drive'

    Returns:
        networkx.Graph: The downloaded OSMnx graph.
    """
    return ox.graph_from_place(place_name, network_type=network_type)

def get_nearest_node(graph, lat, lon):
    """ Gets the nearest node in the OSMnx graph to the specified latitude and longitude.

    Args:
        graph (networkx.Graph): The OSMnx graph.
        lat (float): Latitude of the point.
        lon (float): Longitude of the point.

    Returns:
        int: The nearest node in the graph.
    """
    return ox.distance.nearest_nodes(graph, X=lon, Y=lat)
