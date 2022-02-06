Requirements
===

The following applications and software tooling are required:
* Python >= 3.6
* Poetry 1.12+

Installation instructions:\

Linux:

```sh
# install python3
sudo apt install python3.8

# install poetry 1.12+
curl -sSL https://install.python-poetry.org | python3 -
poetry install

# Run the application
poetry run app
```

Project setup
=============================

* `scripts.py` contains starter functions that can be called using `poetry run`. Useful to start the application or run unit tests.
* `pyproject.toml` contains poetry project dependencies and script definitions.


Running unit tests
============================

We are using unittest framework as provided by python3.

Using the following commands you can run unit tests:

```sh
# using poetry
poetry run app          # runs the application
poetry run test         # runs unit tests
poetry run coverage     # runs unit tests with coverage

# Run a specific unit test file.
poetry run python tests/test_py_polynomial_solver.py

# Run a specific test in the unit test file
poetry run python tests/test_py_polynomial_solver.py TestPolynomialParser.test_quadratic
```



Application follows Model View Controller (MVC) design architecture.
Model: 
