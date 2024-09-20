import osmnx as ox

def download_osm_graph(place_name, network_type='drive'):
    """
    Downloads the OSMnx graph for the specified location.
    
    :param place_name: Name of the place to download the graph for (e.g., 'Helsinki, Finland').
    :param network_type: The type of network to download (e.g., 'drive' for car-accessible roads).
    :return: The downloaded NetworkX graph.
    """
    return ox.graph_from_place(place_name, network_type=network_type)

def get_nearest_node(graph, lat, lon):
    """
    Gets the nearest node in the OSMnx graph to the specified latitude and longitude.
    
    :param graph: The OSMnx graph.
    :param lat: Latitude of the point.
    :param lon: Longitude of the point.
    :return: The nearest node in the graph.
    """
    return ox.distance.nearest_nodes(graph, X=lon, Y=lat)
