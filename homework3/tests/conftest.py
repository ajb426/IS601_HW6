"""
This module contains pytest fixtures for generating test data and configuring pytest.
"""

import random
import pytest
from faker import Faker

def pytest_addoption(parser):
    """
    Adds custom command line options to pytest.
    """
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

@pytest.fixture(scope="session")
def num_records(request):
    """
    Fixture to get the number of records specified by the --num_records option.
    """
    return request.config.getoption("--num_records")

def generate_test_data(record_count):
    """
    Generates test data using Faker.
    """
    fake = Faker()
    test_data = []
    for _ in range(record_count):
        x = float(fake.random_number(digits=2, fix_len=False))
        y = float(fake.random_number(digits=2, fix_len=False))
        operation = random.choice(["add", "subtract", "multiply", "divide"])
        if operation == "add":
            expected = f"The result of {x} add {y} is equal to {x + y:.1f}"
        elif operation == "subtract":
            expected = f"The result of {x} subtract {y} is equal to {x - y:.1f}"
        elif operation == "multiply":
            expected = f"The result of {x} multiply {y} is equal to {x * y:.1f}"
        elif operation == "divide":
            if y == 0:
                expected = "An error occurred: Cannot divide by zero"
            else:
                expected = f"The result of {x} divide {y} is equal to {x / y:.1f}"
        else:
            expected = "Unknown operation"
        test_data.append((str(x), str(y), operation, expected))
    test_data.append(("1", "0", "divide", "An error occurred: Cannot divide by zero"))
    return test_data

@pytest.fixture(scope="session")
def generated_test_data(num_records):
    """
    Fixture to generate test data using the generate_test_data function.
    """
    return generate_test_data(num_records)

@pytest.fixture
def record(request, generated_test_data):
    """
    Fixture to provide a single test record from the generated test data.
    """
    return generated_test_data[request.param]

def pytest_generate_tests(metafunc):
    """
    Custom implementation for parameterizing tests.
    """
    if 'record' in metafunc.fixturenames:
        num_tests = metafunc.config.getoption('num_records')
        metafunc.parametrize('record', range(num_tests), indirect=True)
