# RouteOptimizer - User Guide

## Installation

#### Requirements
- Python 3.10 or newer
- Poetry (for dependency management)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sampsaoinonen/TiRa-RouteOptimizer.git
2. **Move to the project folder:**

    ```bash
    cd TiRa-RouteOptimizer
    ```
    
3. **Install dependencies:**

    Use Poetry to install all the necessary dependencies:

    ```bash
    poetry install
    ```

## Running the Application

**Start the application:**
    
To run the application locally, execute the following command:

```bash
poetry run invoke start
```

**Wait for a while and access the web interface:**

After running the command, open your browser and go to:

```
http://127.0.0.1:5000
```

## Using the Application

![Animated gif](./images/using_the_app.gif)

- Select a start point and a goal point on the map.
- The app will calculate and display routes found using the A* and Fringe Search algorithms. 
- Length and time of both algorithms are shown on the top lef corner. 
- Red is A* and Blue is Fringe Search

## Exiting the Application

To stop the application, simply return to the terminal and press Ctrl + C.

## Possible problems

**OSMnx map not loading:**
- Ensure your internet connection is stable.
- Wait for the OSMnx maps to fully load (this can take a few moments).

**No path found:**
- Make sure the two selected points are connected by streets on the map. Disconnected nodes will return no path.