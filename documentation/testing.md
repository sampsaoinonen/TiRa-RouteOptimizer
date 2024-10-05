# Testing Documentation

## Coverage report


| File                          | Stmts | Miss | Branch | BrPart | Cover | Missing        |
|-------------------------------|-------|------|--------|--------|-------|----------------|
| src/algorithms/a_star.py       | 50    | 0    | 20     | 0      | 100%  | -              |
| src/algorithms/fringe_search.py| 56    | 0    | 20     | 0      | 100%  | -              |
| src/utils/graph_utils.py       | 18    | 0    | 10     | 0      | 100%  | -              |
| src/utils/osm_utils.py         | 5     | 0    | 0      | 0      | 100%  | -              |
| **TOTAL**                      | **129** | **0**  | **50**   | **0**    | **100%** | -              |




To generate a test coverage report, use the following commands:
```bash
poetry run coverage run --branch -m pytest src
```

To generate a test coverage report **wihtout performance testing**: (Note that performance test takes couple minutes to finish)

```bash
poetry run coverage run --branch -m pytest src --ignore=src/tests/performance
```

For a summary of the results on the command line:
```bash
poetry run coverage report -m
```

To generate a separate HTML file for the report:
```bash
poetry run coverage html

## Unit Testing Coverage

The tests focus on verifying the behavior of graph traversal algorithms (A* and Fringe Search) and utility functions using geographic graphs. Key functionalities include:

- **Algorithms Tested:**
  - **AStarOSMnx**: Pathfinding using A* algorithm and comparison Dijkstra.
  - **FringeSearchOSMnx**: Pathfinding using Fringe Search and comparison with Dijkstra.
  - **Utility Functions**: Distance metrics ( Euclidean ) and edge length calculations.


### What Was Tested and How?

#### Pathfinding Tests:

- **Valid Pathfinding**: Both A* and Fringe Search were tested to ensure that they correctly find the shortest path on a simple graph representing Helsinki-based nodes. The path and total length were verified.
  
- **Disconnected Graph**: Edges were removed to create a disconnected graph, and the algorithms were tested to confirm they return no path when nodes are unreachable.

- **Non-existent Nodes**: Scenarios were tested where the start or goal nodes do not exist in the graph to ensure that both algorithms handle such cases gracefully.

- **Handling Cycles**: The algorithms were tested in graphs containing cycles to ensure that they return the shortest path and do not get stuck in loops.

- **Single Node Graph**: Both A* and Fringe Search were tested to ensure they return the correct result when the graph contains only one node.

- **Multiple Shortest Paths**: The algorithms' behavior was tested in cases where there are multiple equally short paths between the start and goal nodes.

- **No Weights on Edges**: Tests ensured that the algorithms handle cases where some edges lack a `length` attribute, using defaults to calculate paths.

#### Comparison to Dijkstra:

- **10 Random Tests**: Both A* and Fringe Search were tested with randomly selected start and goal nodes, and their results were compared with Dijkstra's algorithm to ensure correctness. Path lengths were compared within a tolerance of 1 m.


#### Utility Function Tests:

- **Edge Length**: Validated that `get_edge_length` correctly computes edge lengths between nodes.
- **Distance Metrics**: Verified accuracy of distance metrics (Euclidean) between nodes with geographic coordinates.

### Test Inputs

1. **Graph Data**: Nodes representing real-world locations in Helsinki, Finland.
2. **Randomized Inputs**: Random start-goal pairs for comparing A* and Dijkstra.
3. **Edge Cases**: Scenarios with nonexistent nodes, disconnected graphs, and missing weights were explicitly tested.


### How to Repeat the UnitTests

Tests can be executed with the following command:

```bash
poetry run pytest src/tests/unit 
```

## Integration Testing Coverage

The integration tests focus on verifying the behavior of graph traversal algorithms (A* and Fringe Search) in real-world scenarios using OSMnx data for Helsinki. These tests include random node selection for start and goal points and compare results with Dijkstra's algorithm to ensure consistency in pathfinding.

#### Integration Tests Performed:

- **AStarOSMnx vs. Dijkstra**: Integration tests to compare the A* algorithm with Dijkstra’s algorithm on real-world OpenStreetMap (OSM) data using OSMnx. Random start and goal nodes were selected within Helsinki, and the path lengths were compared.
  
- **FringeSearchOSMnx vs. Dijkstra**: Similar integration tests were performed to compare the Fringe Search algorithm with Dijkstra’s algorithm using random node pairs from OSMnx’s Helsinki graph.

- **OSM Utility Functions**: Tests focused on verifying the utility functions `download_osm_graph` and `get_nearest_node`. The tests ensure that OSMnx correctly retrieves graphs and nodes, even in edge cases like invalid coordinates.

### Integration Test Cases:

#### AStarOSMnx vs. Dijkstra:

- **Random Start and Goal Nodes**: In each test iteration, a random start and goal node were selected from the OSMnx graph of Helsinki. The paths were calculated using both the A* and Dijkstra algorithms, and their lengths were compared to ensure they matched within a small tolerance.
  
- **Handling No Paths**: If the algorithms could not find a path between the randomly selected nodes, the test was skipped. Otherwise, the path lengths were asserted to be nearly identical.

#### FringeSearchOSMnx vs. Dijkstra:

- **Random Start and Goal Nodes**: Similar to the A* tests, random start and goal nodes were selected. The paths computed by the Fringe Search and Dijkstra algorithms were compared to ensure correctness.
  
- **Handling No Paths**: As with the A* tests, cases where no valid path existed were handled gracefully, with no path found and the iteration skipped.

#### OSM Utilities:

- **OSM Graph Download**: The test ensured that the function `download_osm_graph` correctly retrieves a valid graph for Helsinki, Finland.

- **Nearest Node Retrieval**: The function `get_nearest_node` was tested for both valid and invalid coordinates:
  - **Valid Coordinates**: Tested with known points in Helsinki, ensuring the correct nearest node is returned.
  - **Invalid Coordinates**: Used arbitrary invalid coordinates (e.g., in the ocean) to verify the function’s robustness, ensuring it still returned a valid node.

### How to Repeat the Integration Tests
Note that random.seed(42) is used in the integration tests to ensure that the same random start and goal nodes are selected in each test run, making the tests reproducible.

To run these integration tests, use the following command:

```bash
poetry run pytest src/tests/integration
```

### Performance Testing Coverage

Performance tests were added to compare A* and Fringe Search algorithms over 100 random routes using real-world geographic data from the Uusimaa region. These tests measure the execution time of each algorithm and compare the results with Dijkstra's algorithm to ensure correctness.

#### Performance Tests Performed:
- *Algorithm Comparison*: The performance tests focus on comparing the speed and accuracy of A* and Fringe Search algorithms over large maps using OSMnx data. In each test, the start and goal nodes are selected randomly, and the execution times of both algorithms are recorded.
- *Execution Time and Path Length Comparison*: The paths found by A* and Fringe Search are compared to the lengths computed by Dijkstra's algorithm. The test results are plotted to visually compare the performance of both algorithms at different distances.

#### How to Repeat the Performance Tests
Performance tests can be executed using the following command:

```bash
poetry run pytest src/tests/performance
```

Note that this test takes couple minutes to finish.

#### Plotting the Results

The performance tests include code for generating plots that compare the execution times of both A* and Fringe Search algorithms. The results are plotted against the distances of the paths to provide a visual comparison of the algorithms' efficiency.

#### An example of plot created by performance test

![A_star_vs_Fringe_Search_performance_test](./documentation/images/A_star_vs_Fringe_Search_performance_test.jpg)  