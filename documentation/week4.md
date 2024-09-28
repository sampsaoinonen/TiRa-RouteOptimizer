# Weekly Report 4

### What did I do this week?
- Refactored Fringe Search and fixed bug caused not finding shortest route always 
- Fixed edge length handling for MultiGraph to ensure finding always shortest path
- Changed to use only eucledian heurestics(teachers hint)
- Added integration tests for both algorithms using OSMnx data
- Integrated javascript frontend with maps using Leaflet
- Backend now works through Flask
- Graphic interface now shows the routes, length and calculation times

### How has the project progressed?
It is going pretty good. Fringe search couldn't always find the shortest path so I started all over building the fringe and managed to fix it. I've been trying to build frontend with Leaflet starting almost from week 1 and now got some kind of version working. 

### What did I learn this week ?
- Gained deeper knowledge of the Fringe Search algorithm
- Not sure if Javascript is a real language

### What was unclear or caused difficulties?
- At first why the first try Fringe Search wasn't working

### What will I do next?
- Research if Fringe Search can be optimized more...
- How to compare memory usage of these two algorithms (memory-profiler maybe?)


### Hours spent on the project this week:

| Date  | Time Spent | Description                                     |
| ----- | ---------- | ------------------------------------------------|
| 25.9  | 2h         | Studying Fringe and trying to undestand the bug                                |
| 26.9  | 2h         | Fixing the bug, Building front                                 |
| 27.9  | 6h         | Integration tests, Building front        |
| 28.9  | 10h         | Refactor projects file structure, Update testing and documentation, Building front |
| **Total** | **20h**     |