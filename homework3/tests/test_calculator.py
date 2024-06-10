"""
Test suite for the Calculator and Calculation classes.

This module contains tests for the following functionalities:
- Basic arithmetic operations (add, subtract, multiply, divide)
- Exception handling for division by zero
- History management
- String representation and detail retrieval
- Initialization of Calculator instances
"""

import pytest
from faker import Faker
from calculator import Calculator, Calculation

fake = Faker()

@pytest.mark.parametrize("x, y", [
    (fake.random_number(digits=5), fake.random_number(digits=5)),
    (fake.random_number(digits=5), fake.random_number(digits=5)),
    (fake.random_number(digits=5), fake.random_number(digits=5)),
])
def test_add(x, y, expected):
    """
    Test the add method of the Calculator class.
    """
    expected = x + y
    assert Calculator.add(x, y) == expected

@pytest.mark.parametrize("x, y", [
    (fake.random_number(digits=5), fake.random_number(digits=5)),
    (fake.random_number(digits=5), fake.random_number(digits=5)),
    (fake.random_number(digits=5), fake.random_number(digits=5)),
])
def test_subtract(x, y, expected):
    """
    Test the subtract method of the Calculator class.
    """
    expected = x - y
    assert Calculator.subtract(x, y) == expected

@pytest.mark.parametrize("x, y", [
    (fake.random_number(digits=5), fake.random_number(digits=5)),
    (fake.random_number(digits=5), fake.random_number(digits=5)),
    (fake.random_number(digits=5), fake.random_number(digits=5)),
])
def test_multiply(x, y, expected):
    """
    Test the multiply method of the Calculator class.
    """
    expected = x * y
    assert Calculator.multiply(x, y) == expected

@pytest.mark.parametrize("x, y", [
    (fake.random_number(digits=5, fix_len=True), fake.random_number(digits=5, fix_len=True) or 1),
    (fake.random_number(digits=5, fix_len=True), fake.random_number(digits=5, fix_len=True) or 1),
    (fake.random_number(digits=5, fix_len=True), fake.random_number(digits=5, fix_len=True) or 1), 
])
def test_divide(x, y, expected):
    """
    Test the divide method of the Calculator class.
    """
    if y == 0:
        y = 1
    expected = x / y
    assert Calculator.divide(x, y) == expected

def test_divide_by_zero():
    """
    Test division by zero in the Calculator class.
    """
    x = fake.random_number(digits=5)
    assert Calculator.divide(x, 0) == "Error: Division by zero is not allowed."

def test_history():
    """
    Test the history management methods of the Calculator class.
    """
    Calculator.clear_history()
    Calculator.add(fake.random_number(digits=5), fake.random_number(digits=5))
    Calculator.subtract(fake.random_number(digits=5), fake.random_number(digits=5))
    assert len(Calculator.get_history()) == 2
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0

def test_last_calculation():
    """
    Test the get_last_calculation method of the Calculator class.
    """
    Calculator.clear_history()
    Calculator.add(fake.random_number(digits=5), fake.random_number(digits=5))
    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc.result == last_calc.x + last_calc.y

def test_calculation_get_details():
    """
    Test the get_details method of the Calculation class.
    """
    x = fake.random_number(digits=5)
    y = fake.random_number(digits=5)
    calculation = Calculation("+", x, y, x + y)
    details = calculation.get_details()
    assert details == ("+", x, y, x + y)

def test_calculation_repr():
    """
    Test the __repr__ method of the Calculation class.
    """
    x = fake.random_number(digits=5)
    y = fake.random_number(digits=5)
    calculation = Calculation("+", x, y, x + y)
    expected_repr = f"{x} + {y} = {x + y}"
    assert repr(calculation) == expected_repr

def test_calculator_initialization():
    """
    Test the initialization of the Calculator class.
    """
    calculator = Calculator()
    assert calculator.result == 0

def test_get_last_calculation():
    """
    Test the get_last_calculation method of the Calculator class.
    """
    Calculator.clear_history()
    assert Calculator.get_last_calculation() is None  # History is empty, should return None

    Calculator.add(fake.random_number(digits=5), fake.random_number(digits=5))
    Calculator.add(fake.random_number(digits=5), fake.random_number(digits=5))
    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc.operation == "+"
    assert last_calc.result == last_calc.x + last_calc.y

    Calculator.clear_history()
    assert Calculator.get_last_calculation() is None
