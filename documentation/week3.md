# Weekly Report 3

### What did I do this week?
- Studied Fringe Search
- Built a version of the Fringe Search algorithm
- Integrated both A* and Fringe Search algorithms into the main program
- Refactored algorithm files and separated methods for clarity
- Installed pylint and use it to clean up
- Added test for all files except main.py
- Simple usermenu with options for predefined, random, and user-input start and goal coordinates
- Incorporated Manhattan, Euclidean, and Haversine distance calculations for future use

### How has the project progressed?
Both algorithms The A* algorithm and Fringe Search with Haversine heuristics in use are now implemented and tested using the Helsinki OSMnx graph. Visualizations of the shortest path have been created with Matplotlib, and unit tests have been written to ensure the algorithm functions correctly. The program can now be used via a simple user menu.

### What did I learn this week ?
- How Fringe Search works
- Fringe seems not the give always the path thath matches with A* or Dijkstra

### What was unclear or caused difficulties?
- Limited availability of study material on Fringe Search
- Building Fringe Search was difficult
- Picking right heuristics
- Understanding why fringe does not the give always the path that matches with A* or Dijkstra

### What will I do next?
- Research if Fringe Search can be optimized more
- Consider developing a graphical user interface
- Compare the impact of different heuristics(Manhattan, Euclidean, and Haversine) on results and performance

### Hours spent on the project this week:

| Date  | Time Spent | Description                                     |
| ----- | ---------- | ------------------------------------------------|
| 17.9  | 2h         | Studying Fringe                                 |
| 18.9  | 2h         | Studying Fringe                                 |
| 19.9  | 3h         | Building Fringe, Updating app to use both algorithms        |
| 20.9  | 10h         | Refactoring program, usermenu, lint, testing, documentation |
| 21.9  | 1h         | Expand tests for A* and Fringe, update documentation |
| **Total** | **18h**     |