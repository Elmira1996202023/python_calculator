import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver 3")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
