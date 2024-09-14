# RouteOptimizer

  

**RouteOptimizer** is a navigational tool that uses and compares multiple pathfinding algorithms to find the most efficient route in a city street network. The project allows users to simulate and visualize shortest path searches and evaluate the performance of used algorithms.

  

This project is part of the **Helsinki University course**: _Aineopintojen harjoitustyö: Algoritmit ja tekoäly TKT20010_.

---

## Documentation
- [Specifications](./documentation/specifications.md)

## Weekly Reports
- [Week 1](./documentation/week1.md)
- [Week 2](./documentation/week2.md)

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

Tests can be executed with the following command
```bash
poetry run pytest src
```

### Test coverage

To generate a test coverage report, use the following commands:
```bash
poetry run coverage run --branch -m pytest src
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
poetry run python src/main.py
```