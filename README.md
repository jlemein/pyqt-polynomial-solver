(in progress)
This project is created to serve as educational content on what it means to design according to the model view controller (MVC) design or paradigm.
This is a polynomial solver and plotter. Evidently we need a concept of a **polynomial**. A polynomial forms our model.
The model can in theorey come from anywhere, such as from a database or from any other data source. In this case the polynomial comes from an interactable dialog. The controller
is responsible for loading data into the polynomial model.

The following **models** are present:
* An equation interface that requires one implementation that returns the equation as a string in Latex notation.
* A polynomial object which represents polynomial equations. A `Polynomial` is a `Equation`.

There are a couple of **views**:
* The mathematical equation label to display the represented polynomial equation.
* A 2D graph plot visually displaying the equation.
* A polynomial editor, in which you can interact with the polynomial.

The controllers are present in the following form:
* (still to come)

# Requirements

The following applications and software tooling are required:
* Python >= 3.6
* Poetry 1.12+

Installation instructions:\

Linux:

```sh
# install python version >= 3.6. Here we install python 3.8.
sudo apt install python3.8

# install latest poetry (1.12+)
curl -sSL https://install.python-poetry.org | python3 -
poetry install

# Run the application
poetry run app

# Run unit tests
poetry run test
```

# Project setup

* `scripts.py` contains starter functions that can be called using `poetry run`. Useful to start the application or run unit tests.
* `pyproject.toml` contains poetry project dependencies and script definitions.

# Architecture decision

Application follows Model View Controller (MVC) design architecture.
In short
 
 * A model and view will never communicate directly with each other. It goes via the controller.
 * The visualization (view) is decoupled from the internal data representation (model).
 * Controller makes sure a model is read and updated.
 * Controller passes the data from the model to the view.

## Running unit tests

We are using unittest framework as provided by python3.

Using the following commands you can run unit tests:

```sh
# using poetry
poetry run test         # runs unit tests
poetry run coverage     # runs unit tests with coverage

# Run a specific unit test file.
poetry run python tests/test_py_polynomial_solver.py

# Run a specific test in the unit test file
poetry run python tests/test_py_polynomial_solver.py TestPolynomialParser.test_quadratic
```
