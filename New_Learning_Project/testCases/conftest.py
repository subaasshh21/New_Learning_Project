import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
