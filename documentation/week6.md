# Weekly Report 6

### What did I do this week?
- Refactored performance tests and added workflow to GitHub Actions.
- Performance tests are in different workflow which is run manually(Takes about 20 minutes)
- Implemented automated artifact saving for performance plots.
- Added Invoke for task automation and created tasks for testing, linting, and performance testing.
- Fixed indentation and log saving issues in GitHub Actions workflow.
- Updated Codecov integration and added badges for workflow status and code coverage.
- Added handling of missing node coordinates in graph utilities
- Fixed Dijkstra result to return float('inf') when no path is found instead of None
- Set up unit tests to run every time the app starts (teacher's recommendation)


### How has the project progressed?
Good. This week I did a lot of small things. In the background, I continued trying to do different optimized versions of Fringe, but they're still all slower than A*.

### What did I learn this week ?
- Refreshed  my memory of workflows and using Invoke
- How to save artifacts using workflows

### What was unclear or caused difficulties?
- Commands in workflows
- Same old optimizing Fringe

### What will I do next?
- Documentation updates
- Implement optimized version of Fringe
- More informative prints to terminal on tests and in using the app


### Hours spent on the project this week:

| Date  | Time Spent | Description                                     |
| ----- | ---------- | ------------------------------------------------|
| 7.10  | 7h         | Codecov, Workflows                             |
| 8.10  | 2h         | Trying to optimize Fringe                             |
| 11.10  | 7h         | Invoke, edit tests, animated gif, documentation update          |
| 12.10  | 3h         | documentation update          |

| **Total** | **19h**     |