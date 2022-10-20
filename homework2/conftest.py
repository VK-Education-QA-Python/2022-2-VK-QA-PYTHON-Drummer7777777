import os.path
import shutil
import sys
import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from ui.pages.base_page import BasePage
import creds
from ui.pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target-sandbox.my.com')
    parser.addoption('--headless', action='store_true')
    parser.addoption('--debug_log', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    headless = request.config.getoption('--headless')
    debug_log = request.config.getoption('--debug_log')
    return {
        'browser': browser,
        'url': url,
        'headless': headless,
        'debug_log': debug_log,
    }


@pytest.fixture()
def driver(config):
    options = Options()
    options.headless = config['headless']
    if config['browser'] == 'chrome':
        # browser = webdriver.Chrome(executable_path=ChromeDriverManager(version='102.0.5005.61').install(),options=options)
        browser = webdriver.Chrome(executable_path=ChromeDriverManager(version="105.0.5195.19").install(),options=options)
    browser.get(config['url'])
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config)
    driver.get(config['url'])
    login_page = LoginPage(driver)
    login_page.login(*credentials)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies

def get_driver(config):
    options = Options()
    options.headless = config['headless']
    if config['browser'] == 'chrome':
        # browser = webdriver.Chrome(executable_path=ChromeDriverManager(version='102.0.5005.61').install(),options=options)
        browser = webdriver.Chrome(executable_path=ChromeDriverManager(version='105.0.5195.19').install())
    return browser


@pytest.fixture(scope='session')
def credentials():
    return creds.LOGIN, creds.PASSWORD

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))

@pytest.fixture()
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'tigr.jpeg')

@pytest.fixture()
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture(scope='session')
def base_temp_dir():
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    return base_dir

@pytest.fixture(scope='function')
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

