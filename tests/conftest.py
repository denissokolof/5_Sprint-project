import pytest
import random

@pytest.fixture
def random_email():
        return f"{random.randint(1000, 100000)}denis{random.randint(10000, 10000000)}@ya.ru"

@pytest.fixture
def login_for_():
        return f"{random.randint(1000, 100000)}denis{random.randint(10000, 10000000)}@ya.ru"