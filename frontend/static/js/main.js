// Initialize the map centered at Helsinki coordinates.
var map = L.map('map').setView([60.1699, 24.9384], 13);  // Helsinki coordinates

// Add OpenStreetMap tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Variables to hold start and goal markers and polylines for both routes
var startMarker, goalMarker;
var fringePolyline, aStarPolyline;
var selectingStart = true;  // Start by selecting the start point
var timeoutActive = false;  // Prevent fast consecutive selections that causes errors using Safari 

/**
 * Updates the displayed route length and time taken for the given algorithm.
 *
 * @param {String} algorithm - The name of the algorithm ('fringe' or 'astar').
 * @param {Number} length - The length of the route in meters.
 * @param {Number} timeTaken - The time taken to compute the route in seconds.
 */
function updateRouteInfo(algorithm, length, timeTaken) {
    if (algorithm === 'fringe') {
        document.getElementById('fringe-length').innerText = `Fringe Search Route Length: ${length.toFixed(2)} meters | Time Taken: ${timeTaken.toFixed(2)} seconds`;
    } else if (algorithm === 'astar') {
        document.getElementById('astar-length').innerText = `A* Route Length: ${length.toFixed(2)} meters | Time Taken: ${timeTaken.toFixed(2)} seconds`;
    }
}

/**
 * Adds the route to the map and applies a slight offset to prevent overlapping routes.
 *
 * @param {Array} routeCoordinates - Array of [latitude, longitude] pairs for the route.
 * @param {String} algorithm - The algorithm used for the route ('fringe' or 'astar').
 * @param {Number} length - The length of the route in meters.
 * @param {Number} timeTaken - The time taken to compute the route in seconds.
 */
function addRouteToMap(routeCoordinates, algorithm, length, timeTaken) {
    /**
     * Offsets the coordinates slightly to avoid overlap between multiple routes.
     *
     * @param {Array} coords - Array of [lat, lng] coordinates.
     * @param {Number} offsetAmount - Amount by which to offset the coordinates.
     * @returns {Array} New array with offset coordinates.
     */
    function offsetCoordinates(coords, offsetAmount) {
        return coords.map(coord => [coord[0] + offsetAmount, coord[1] + offsetAmount]);
    }

    // Update the route length and time for the selected algorithm
    updateRouteInfo(algorithm, length, timeTaken);

    if (algorithm === 'fringe') {
        if (fringePolyline) {
            map.removeLayer(fringePolyline);
        }
        var offsetFringeRoute = offsetCoordinates(routeCoordinates, 0.00002);
        fringePolyline = L.polyline(offsetFringeRoute, { color: 'blue' }).addTo(map);
    } else if (algorithm === 'astar') {
        if (aStarPolyline) {
            map.removeLayer(aStarPolyline);
        }
        var offsetAStarRoute = offsetCoordinates(routeCoordinates, -0.00002);
        aStarPolyline = L.polyline(offsetAStarRoute, { color: 'red' }).addTo(map);
    }
}

/**
 * Resets the start and goal markers and removes drawn routes from the map.
 */
function resetMarkersAndRoute() {
    // Remove previous start marker
    if (startMarker) {
        map.removeLayer(startMarker);
    }
    // Remove previous goal marker
    if (goalMarker) {
        map.removeLayer(goalMarker);
    }
    // Remove previous Fringe Search route
    if (fringePolyline) {
        map.removeLayer(fringePolyline);
    }
    // Remove previous A* route
    if (aStarPolyline) {
        map.removeLayer(aStarPolyline);
    }
    selectingStart = true;  // Return to start point selection mode
}

/**
 * Handles the click event on the map.
 * Allows the user to select start and goal points and requests routes from the server.
 *
 * @param {Object} e - The Leaflet map click event containing the clicked coordinates.
 */
function onMapClick(e) {
    // Prevent interaction if timeout is active
    if (timeoutActive) {
        console.log("Wait before selecting the next point.");
        return;
    }

    console.log("Map clicked at", e.latlng);

    if (selectingStart) {
        // Set the start marker
        resetMarkersAndRoute();
        console.log("Setting start marker");
        startMarker = L.marker(e.latlng).addTo(map).bindPopup("Start").openPopup();
        console.log("Start marker set", startMarker);
        selectingStart = false;  // Next, select the goal point

        // Prevent too fast goal selection
        timeoutActive = true;
        setTimeout(function() {
            timeoutActive = false;
        }, 10);

    } else {
        // Set the goal marker and request routes
        console.log("Setting goal marker");
        goalMarker = L.marker(e.latlng).addTo(map).bindPopup("Goal").openPopup();
        console.log("Goal marker set", goalMarker);

        // Request the Fringe Search route from the backend
        fetch('/calculate-fringe-route', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                start: startMarker.getLatLng(),
                goal: goalMarker.getLatLng()
            })
        })
        .then(response => response.json())
        .then(data => {
            addRouteToMap(data.routeCoordinates, 'fringe', data.length, data.timeTaken);  // Draw the route on the map and show length and time
        })
        .catch(error => console.error('Error:', error));

        // Request the A* route from the backend
        fetch('/calculate-astar-route', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                start: startMarker.getLatLng(),
                goal: goalMarker.getLatLng()
            })
        })
        .then(response => response.json())
        .then(data => {
            addRouteToMap(data.routeCoordinates, 'astar', data.length, data.timeTaken);  // Draw the route on the map and show length and time
        })
        .catch(error => console.error('Error:', error));

        // Return to start point selection mode
        selectingStart = true;

        // Prevent too fast start selection after route drawing
        timeoutActive = true;
        setTimeout(function() {
            timeoutActive = false;
        }, 10);
    }
}

// Attach the click event handler to the map
map.on('click', onMapClick);
