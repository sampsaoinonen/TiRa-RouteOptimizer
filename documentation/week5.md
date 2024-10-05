# Weekly Report 5

### What did I do this week?
- Peer [review](https://github.com/reettap/calculator/issues/1)
- Commented peer [review](https://github.com/sampsaoinonen/TiRa-RouteOptimizer/issues/1) of my work
- Refactored A* and Fringe Search algorithms to improve readability with more comments and clearer code structure. This was also mentioned in peer review of my work.
- Added performance test to compare A* and Fringe Search algorithms, verifying correctness with Dijkstra
- Made different optimized versions of Fringe Search
- Pylinted the code

### How has the project progressed?
It's going okay. The algorithms are pretty complex to understand at first sight so I tried to help the reading with comments and better structure. Hannu Kärnä suggested to performance test algorithms with bigger area and more repetitions(100) which I did. I tried to optimized Fringe with different ways but it's still losing to A* in speed.

### What did I learn this week ?
- More about testing (Hannu Kärnä lecture)
- Matplotlib for plotting performance comparisons

### What was unclear or caused difficulties?
- Is it possible to make Fringe Search faster than A* if using OSMnx? How could my version of Fringe be optimized more? The [original study](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf) used Fringe Search in grid-based game pathfinding.
- Now I'm testing basicly the same thing in integration testing and performance testing but in different scale. I’m unsure if this is the best way to structure the tests?

### What will I do next?
- How to compare memory usage of these two algorithms (memory-profiler maybe?)
- Add some of the tests run always at first when starting the app(Hannu Kärnä's suggestion)
- Fringe Search optimizing
- Update documentation



### Hours spent on the project this week:

| Date  | Time Spent | Description                                     |
| ----- | ---------- | ------------------------------------------------|
| 1.10  | 4h         | Studying shunting yard,  reviewed a peer project.                                |
| 2.10  | 2h         | Writing peer review          |
| 3.10  | 6h         | Commenting peer review, Trying to optimize Fringe, Refactoring and commenting algorithms        |
| 4.10  | 4h         | Refactoring and commenting algorithms, Creating performance test|
| 5.10  | 6h         | Creating performance test, Pylinting, Documentation update|
| **Total** | **22h**     |