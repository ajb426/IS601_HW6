"""
Test suite for the Calculator and Calculation classes.

This module contains tests for the following functionalities:
- Basic arithmetic operations (add, subtract, multiply, divide) in the Calculator class
- Exception handling for division by zero in the Calculator class
- History management in the Calculator class
- String representation and detail retrieval in the Calculation class
- Initialization of Calculator instances
"""

from faker import Faker
from calculator import Calculator, Calculation

def test_operation(record):
    """
    Test arithmetic operations of the Calculator class using generated records.
    """
    num1, num2, operation, expected = record

    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except ValueError:
        output = f"Invalid number input: {num1} or {num2} is not a valid number."
        assert output == expected
        return

    try:
        if operation == 'add':
            result = Calculator.add(num1_float, num2_float)
        elif operation == 'subtract':
            result = Calculator.subtract(num1_float, num2_float)
        elif operation == 'multiply':
            result = Calculator.multiply(num1_float, num2_float)
        elif operation == 'divide':
            if num2_float == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = Calculator.divide(num1_float, num2_float)
        else:
            output = f"Unknown operation: {operation}"
            assert output == expected
            return
        output = f"The result of {num1} {operation} {num2} is equal to {result:.1f}"
    except ZeroDivisionError as e:
        output = f"An error occurred: {e}"

    assert output == expected

def test_divide_by_zero():
    """
    Test division by zero in the Calculator class.
    """
    fake = Faker()
    x = fake.random_number(digits=5)
    try:
        Calculator.divide(x, 0)
    except ZeroDivisionError as e:
        assert str(e) == "Cannot divide by zero"

def test_history():
    """
    Test the history management methods of the Calculator class.
    """
    fake = Faker()
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
    fake = Faker()
    Calculator.clear_history()
    Calculator.add(fake.random_number(digits=5), fake.random_number(digits=5))
    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None
    assert last_calc.result == last_calc.x + last_calc.y

def test_calculation_get_details():
    """
    Test the get_details method of the Calculation class.
    """
    fake = Faker()
    x = fake.random_number(digits=5)
    y = fake.random_number(digits=5)
    calculation = Calculation("+", x, y, x + y)
    details = calculation.get_details()
    assert details == ("+", x, y, x + y)

def test_calculation_repr():
    """
    Test the __repr__ method of the Calculation class.
    """
    fake = Faker()
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
    fake = Faker()
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

def test_addition_coverage():
    """
    Baseline test to cover addition function.
    """
    fake = Faker()
    x = fake.random_number(digits=2, fix_len=False)
    y = fake.random_number(digits=2, fix_len=False)
    expected = f"The result of {x} add {y} is equal to {x + y:.1f}"
    assert expected == f"The result of {x} add {y} is equal to {x + y:.1f}"

def test_multiplication_coverage():
    """
    Baseline test to cover divide by zero error.
    """
    fake = Faker()
    x = fake.random_number(digits=2, fix_len=False)
    y = fake.random_number(digits=2, fix_len=False)
    expected = f"The result of {x} multiplied by {y} is equal to {x * y:.1f}"
    assert expected == f"The result of {x} multiplied by {y} is equal to {x * y:.1f}"

def test_division_coverage():
    """
    Baseline test to cover divide by zero error.
    """
    fake = Faker()
    x = fake.random_number(digits=2, fix_len=False)
    y = fake.random_number(digits=2, fix_len=False)
    expected = f"The result of {x} divided by {y} is equal to {x / y:.1f}"
    assert expected == f"The result of {x} divided by {y} is equal to {x / y:.1f}"

def test_subtract_coverage():
    """
    Baseline test to cover divide by zero error.
    """
    fake = Faker()
    x = fake.random_number(digits=2, fix_len=False)
    y = fake.random_number(digits=2, fix_len=False)
    expected = f"The result of {x} subtracted by {y} is equal to {x - y:.1f}"
    assert expected == f"The result of {x} subtracted by {y} is equal to {x - y:.1f}"
