import pytest
from faker import Faker
import random

def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

@pytest.fixture(scope="session")
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture(scope="session")
def generated_test_data(num_records):
    fake = Faker()
    test_data = []
    for _ in range(num_records):
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
        test_data.append((str(x), str(y), operation, expected))
    return test_data

@pytest.fixture
def record(request, generated_test_data):
    return generated_test_data[request.param]

def pytest_generate_tests(metafunc):
    if 'record' in metafunc.fixturenames:
        num_records = metafunc.config.getoption('num_records')
        metafunc.parametrize('record', range(num_records), indirect=True)
