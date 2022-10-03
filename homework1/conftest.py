import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true")

@pytest.fixture()
def config(request):
    headless = request.config.getoption("--headless")
    return {"headless": headless}

@pytest.fixture(scope='function')
def driver(config):
    options = Options()
    options.headless = config["headless"]
    driver = webdriver.Chrome(executable_path=ChromeDriverManager(version='102.0.5005.61').install(),options=options)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager(version="105.0.5195.19").install(),options=options)
    driver.set_window_size(1920,1080)
    driver.implicitly_wait(5)
    driver.get('https://target-sandbox.my.com')
    yield driver
    driver.quit()
