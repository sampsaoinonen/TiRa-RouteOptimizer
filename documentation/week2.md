# Weekly Report 2

### What did I do this week?
- Set up Poetry for dependency management
- Built a version of the A* algorithm with the Haversine heuristic
- Used OSMnx and Matplotlib dependencies for handling maps and visualizations
- Tested the A* algorithm with the Helsinki OSMnx graph and created route visualizations using Matplotlib
- Wrote unit tests for the A* algorithm
- Compared the performance of the A* algorithm with NetworkX's built-in Dijkstra in unit tests
- Implemented test coverage tracking with Coverage.py
- Focused on writing clear docstrings and comments

### How has the project progressed?
The A* algorithm with Haversine heuristic has been successfully implemented and tested using the Helsinki OSMnx graph. Visualizations of the shortest path have been created with Matplotlib, and unit tests have been written to ensure the algorithm functions correctly. Comparisons between the A* algorithm and NetworkX’s Dijkstra have been integrated into the tests. Test coverage tracking has also been established.

However, I realized that the current solution, which relies on OSMnx and NetworkX graphs, goes against the course guidelines, which suggest not using a graph object. This will require changes to the code to comply with the instructions.

### What did I learn this week / today?
- There are different ways to calculate distances between points, such as Manhattan, Euclidean, and Haversine...
- I gained a deeper understanding of several pathfinding algorithms.

### What was unclear or caused difficulties?
- Integrating the complexities of OSMnx graphs with simplified NetworkX graphs 
- Fringe Search is still under study and needs more focus.

### What will I do next?
- Modify the solution to comply with the guidelines by avoiding graph objects and instead using a simpler       representation
- Implement the Fringe Search algorithm
- Research the technology to be used for the user interface

### Hours spent on the project this week:

| Date  | Time Spent | Description                                     |
| ----- | ---------- | ------------------------------------------------|
| 10.9  | 2h         | Studying A* and Fringe                          |
| 11.9  | 2h         | Studying A* and Fringe                          |
| 12.9  | 2h         | Planning Week 2 implementations, asking for guidance from the teacher |
| 13.9  | 5h         | Algorithm draft, exploring OSMnx and Matplotlib |
| 14.9  | 6h         | Implementation based on previous plans, testing, documentation |
| **Total** | **17h**     |                                                 |
