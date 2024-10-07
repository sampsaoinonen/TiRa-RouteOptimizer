# RouteOptimizer

![GHA workflow badge](https://github.com/sampsaoinonen/TiRa-RouteOptimizer/actions/workflows/main.yml/badge.svg) [![codecov](https://codecov.io/github/sampsaoinonen/TiRa-RouteOptimizer/graph/badge.svg?token=j15hmzwRCQ)](https://codecov.io/github/sampsaoinonen/TiRa-RouteOptimizer)
  
  

**RouteOptimizer** is a navigational tool that uses and compares A* and Fringe Search pathfinding algorithms to find the most efficient route in [Helsinki capital region](https://en.wikipedia.org/wiki/Helsinki_capital_region) street network. The project allows users to simulate and visualize shortest path searches and evaluate the performance of used algorithms.

  

This project is part of the **Helsinki University course**: _Aineopintojen harjoitustyö: Algoritmit ja tekoäly TKT20010_.

---

## Documentation
- [Specifications](./documentation/specifications.md)
- [Testing](./documentation/testing.md)
- [Implementation](./documentation/implementation.md)

## Weekly Reports
- [Week 1](./documentation/week1.md)
- [Week 2](./documentation/week2.md)
- [Week 3](./documentation/week3.md)
- [Week 4](./documentation/week4.md)
- [Week 5](./documentation/week5.md)

## Installation

Clone the repository, navigate to the project's root directory and install the dependencies with the command:
```bash
poetry install
```
You can activate the virtual environment with the command:
```bash
poetry shell
```

In the virtual environment you can leave out poetry run from following commands.

## Command Line Operations
### Testing

All tests can be executed with the following command
```bash
poetry run pytest src
```

Unit tests can be executed with the following command
```bash
poetry run pytest src/test/unit
```

Integration tests can be executed with the following command
```bash
poetry run pytest src/test/integration
```

Performance tests can be executed with the following command

```bash
poetry run pytest src/tests/performance
```

Rest of the tests **wihtout performance testing**: (Note that performance test takes couple minutes to finish)

```bash
poetry run pytest src --ignore=src/tests/performance
```

### Test coverage

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
```
### Running the Main Program
To run the main program, execute the following command:
```bash
poetry run python src/app.py
```

Wait for OSMnx maps to load and open your browser in **http://127.0.0.1:5000**