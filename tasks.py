from invoke import task

@task
def start(c):
    """Run the app."""
    c.run("poetry run pytest -s src/tests/unit")
    c.run("poetry run python src/app.py")

@task
def all_tests(c):
    """Run all tests including performance tests."""
    c.run("poetry run coverage run --branch -s pytest src/tests")

@task
def tests(c):
    """Run the tests excluding performance tests."""
    c.run("poetry run coverage run --branch -m pytest src/tests -k 'not performance'")

@task
def unit_tests(c):
    """Run the unit tests."""
    c.run("poetry run coverage run --branch -m pytest src/tests/unit")

@task
def integration_tests(c):
    """Run the integration tests."""
    c.run("poetry run coverage run --branch -m pytest src/tests/integration")
    
@task
def performance_tests(c):
    """Run performance tests, save plot and performance-log in /test-results"""
    c.run("mkdir -p test-results") # Create test-results directory if it doesn't exist
    c.run("poetry run pytest -s src/tests/performance | tee test-results/performance-log.txt", pty=True)

@task
def lint(c):
    """Run Pylint with a min 9.8/10 rating."""
    c.run("poetry run pylint src --fail-under=9.8")

@task
def coverage_report(c):
    """Generate a coverage report as html and show results in terminal."""
    c.run("poetry run coverage report -m")
    c.run("poetry run coverage html")
