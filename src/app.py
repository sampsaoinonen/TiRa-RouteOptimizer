from flask import Flask, request, jsonify
from flask import send_from_directory
import time
from utils.osm_utils import download_osm_graph, get_nearest_node
from algorithms.fringe_search import FringeSearchOSMnx
from algorithms.a_star import AStarOSMnx

app = Flask(__name__)

# Load the graph
graph = download_osm_graph('Helsinki, Finland')


@app.route('/calculate-fringe-route', methods=['POST'])
def calculate_fringe_route():
    """
    Calculate the route using the Fringe Search algorithm.

    This endpoint receives start and goal coordinates and calculates the 
    shortest route between them using the Fringe Search algorithm.

    Returns:
        JSON response with the route coordinates, total route length (in meters), 
        and the time taken to compute the route.
        Returns a 404 error if no route is available.

    Raises:
        404: If no route is found between the start and goal nodes.
    """
    data = request.json
    start_coords = data['start']
    goal_coords = data['goal']

    # Find the nearest nodes to the start and goal points
    start_node = get_nearest_node(graph, start_coords['lat'], start_coords['lng'])
    goal_node = get_nearest_node(graph, goal_coords['lat'], goal_coords['lng'])

    # Start timing the route calculation
    start_time = time.time()

    # Calculate the route using Fringe Search algorithm
    fs = FringeSearchOSMnx(graph)
    path, length = fs.find_path(start_node, goal_node)

    # Stop timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    if path is None:
        return jsonify({"error": "No route found"}), 404

    # Convert node path to map coordinates (latitude, longitude)
    route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in path]

    return jsonify({
        "routeCoordinates": route_coords,
        "length": length,
        "timeTaken": elapsed_time
    })


@app.route('/calculate-astar-route', methods=['POST'])
def calculate_astar_route():
    """
    Calculate the route using the A* algorithm.

    This endpoint receives start and goal coordinates and calculates the 
    shortest route between them using the A* algorithm.

    Returns:
        JSON response with the route coordinates, total route length (in meters), 
        and the time taken to compute the route.
        Returns a 404 error if no route is available.

    Raises:
        404: If no route is found between the start and goal nodes.
    """
    data = request.json
    start_coords = data['start']
    goal_coords = data['goal']

    # Find the nearest nodes to the start and goal points
    start_node = get_nearest_node(graph, start_coords['lat'], start_coords['lng'])
    goal_node = get_nearest_node(graph, goal_coords['lat'], goal_coords['lng'])

    # Start timing the route calculation
    start_time = time.time()

    # Calculate the route using A* algorithm
    astar = AStarOSMnx(graph)
    path, length = astar.find_path(start_node, goal_node)

    # Stop timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    if path is None:
        return jsonify({"error": "No route found"}), 404

    # Convert node path to map coordinates (latitude, longitude)
    route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in path]

    return jsonify({
        "routeCoordinates": route_coords,
        "length": length,
        "timeTaken": elapsed_time
    })


@app.route('/')
def serve_index():
    """
    Serve the index.html file as the default route.

    Returns:
        The index.html file from the root directory.
    """
    return send_from_directory('../frontend', 'index.html')

@app.route('/style.css')
def serve_css():
    """
    Serve the CSS file for the frontend.

    Returns:
        The 'style.css' file located in the 'frontend/static/css' directory.
    """
    return send_from_directory('../frontend/static/css', 'style.css')

@app.route('/main.js')
def serve_js():
    """
    Serve the main.js for the frontend.

    Returns:
        The 'main.js' file located in the 'frontend/static/js' directory.
    """
    return send_from_directory('../frontend/static/js', 'main.js')

if __name__ == '__main__':
    app.run(debug=True)
