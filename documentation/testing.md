# Testing Documentation

### Unit Testing Coverage

The tests focus on verifying the behavior of graph traversal algorithms (A* and Fringe Search) and utility functions using geographic graphs. Key functionalities include:

- **Algorithms Tested:**
  - **AStarOSMnx**: Pathfinding using A* algorithm on a geographic graph.
  - **FringeSearchOSMnx**: Pathfinding using Fringe Search and comparison with A* and Dijkstra.
  - **Utility Functions**: Distance metrics (Haversine, Euclidean, Manhattan) and edge length calculations.

### Coverage report


| File                          | Stmts | Miss | Branch | BrPart | Cover | Missing        |
|-------------------------------|-------|------|--------|--------|-------|----------------|
| src/algorithms/a_star.py       | 40    | 1    | 20     | 1      | 97%   | 57             |
| src/algorithms/fringe_search.py| 52    | 0    | 24     | 0      | 100%  | -              |
| src/utils/graph_utils.py       | 41    | 0    | 14     | 0      | 100%   | -         |
| src/utils/osm_utils.py         | 5     | 0    | 0      | 0      | 100%  | -              |
| **TOTAL**                      | **138** | **1**  | **58**   | **3**    | **99%** | -              |



### What Was Tested and How?

#### Pathfinding Tests:

- **Valid Pathfinding**: Tested A* and Fringe Search for finding the shortest path on a Helsinki-based graph (node 1 to node 4). Verified path and total length.
- **Disconnected Graph**: Removed edges and verified that algorithms handle cases with no valid path.
- **Non-existent Nodes**: Tested scenarios where start or goal nodes are missing from the graph.
- **Handling Cycles**: Tested if both algorithms correctly handle cycles in the graph, ensuring they return the shortest path despite the presence of loops.
- **Single Node Graph**: Verified that A* and Fringe Search return the correct result when the graph contains only a single node.
- **Multiple Shortest Paths**: Tested how the algorithms behave when multiple equally short paths exist between the start and goal nodes.
- **No Weights on Edges**: Tested the algorithms' behavior when edges without assigned weights are present.


#### Comparison to Dijkstra:

- **10 Random Tests**: Random start and goal nodes tested for A* and Dijkstra algorithms, ensuring path lengths are within a 0.01 km tolerance.

#### Utility Function Tests:

- **Edge Length**: Validated that `get_edge_length` correctly computes edge lengths between nodes.
- **Distance Metrics**: Verified accuracy of distance metrics (Haversine, Euclidean, Manhattan) between nodes with geographic coordinates.

### Test Inputs

1. **Graph Data**: Nodes representing real-world locations in Helsinki, Finland.
2. **Randomized Inputs**: Random start-goal pairs for comparing A* and Dijkstra.
3. **Edge Cases**: Nonexistent nodes and disconnected graphs.

### How to Repeat the Tests

Tests can be executed with the following command:

```bash
poetry run pytest src
```
To generate a test coverage report, use the following commands:
```bash
poetry run coverage run --branch -m pytest src
```

For a summary of the results on the command line:
```bash
poetry run coverage report -m
```
