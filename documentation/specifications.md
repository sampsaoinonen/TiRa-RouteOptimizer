# Specification Document for RouteOptimizer

  

  

## 1. Programming Languages

**In this project:**
  

-  **Primary Language**: Python is being used to implement the core algorithms A* and Fringe Search, as well as handling the backend of the application with Flask.
  

-  **Frontend**: The user interface (UI) is developed using **JavaScript** for rendering and interactivity of the street network and route visualizations.

  

  

**I can peer review projects written in the following languages:**

  

- Python

 

- Javascript

  

- Java

  
- SQL
  

## 2. Algorithms and Data Structures

  

-  **Algorithms used**:

  

-  **A***: Pathfinding algorithm that combines Dijkstra’s shortest path algorithm with a heuristic to guide the search.

  

-  **Fringe Search**: A variation of A* optimized for memory usage, useful for large graphs.

  

  

## 3. Problem to Solve

  

- The primary problem is finding the shortest and most efficient path between two points (intersections) in a city street network. The project will compare the efficiency of A* and Fringe Search pathfinding algorithms in terms of execution time and memory usage.

  

## 4. Input and Usage

  

-  **Input**: The program will use **OSMnx** to retrieve street network data as input, representing the city street network as a graph with nodes (intersections) and edges (streets). Users will interact with this network by selecting start and destination points. They may also optionally add obstacles such as closed roads or increased weights for traffic.

  

-  **Usage**:

  

- The algorithms A* and Fringe Search will find the shortest path between the start and destination points.

- The resulting path, along with performance metrics (e.g., execution time, memory usage), will be displayed to the user on a map rendered via Leaflet and the OSMnx street network.

  

## 5. References

  

- Wikipedia articles on [A*](https://en.wikipedia.org/wiki/A*_search_algorithm), [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) and [Fringe Search](https://en.wikipedia.org/wiki/Fringe_search) on understanding of these algorithms. [Fringe Search study](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf)

  
  

  

## 6. Core Focus of the Project

  

- The core of this project is the **pathfinding algorithms**, specifically comparing algorithms such as A* and Fringe Search in terms of performance and effectiveness in solving the shortest path problem on a city street network.

  

-  **Visualization** and **network rendering** are supporting components that help users interact with the system but are secondary to the algorithms' implementation and analysis.

  

  

## 7. Study Program

  

- I am enrolled in the **Bachelor’s in Computer Science (bSc)** program at the University of Helsinki.

  

- This specification and all documentation for the project will be written in **English**.