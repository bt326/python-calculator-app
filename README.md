# Python Command-Line Calculator

This project is a command-line calculator built using Python.
It supports basic arithmetic operations and follows best practices
such as testing, documentation, and continuous integration.

---

## Features

- Interactive REPL
- Addition, Subtraction, Multiplication, Division
- Input validation
- Error handling
- Unit testing with pytest
- Parameterized tests
- 100% test coverage
- GitHub Actions CI

---

## Project Structure

python-calculator-app/
|
|-- app/
|   |-- __init__.py
|   |-- operations.py
|   |-- repl.py
|
|-- tests/
|   |-- test_operations.py
|   |-- test_repl.py
|
|-- .github/workflows/
|   |-- ci.yml
|
|-- main.py
|-- requirements.txt
|-- pytest.ini
|-- README.md

---

## Setup Instructions

1. Clone the repository

git clone https://github.com/bt326/python-calculator-app.git
cd python-calculator-app

2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

---

## Run Application

python main.py

Follow the prompts to perform calculations.

---

## Run Tests

Run tests:

PYTHONPATH=. pytest

Run tests with coverage:

PYTHONPATH=. python -m pytest --cov=app

---

## Continuous Integration

GitHub Actions runs tests automatically on every push.
Build fails if coverage is below 100%.

---

## Technologies Used

- Python 3.11
- pytest
- pytest-cov
- GitHub Actions

