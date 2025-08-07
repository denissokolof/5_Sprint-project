import pytest
import random
from selenium import webdriver

@pytest.fixture
def driver():
        driver = webdriver.Chrome()
        yield driver
        driver.quit()