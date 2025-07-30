import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    driver=webdriver.chrome(ChromeDriverManager().install())
    return driver
