import os.path
import pytest
from api.client import ApiClient
import creds


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://target-sandbox.my.com')
    parser.addoption('--debug_log', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')
    return {
        'browser': browser,
        'url': url,
        'debug_log': debug_log,
    }

@pytest.fixture(scope='session')
def credentials():
    return creds.LOGIN, creds.PASSWORD

@pytest.fixture(scope='session')
def api_client(credentials, config):
    return ApiClient(base_url = config['url'], login=credentials[0], password=credentials[1])

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))

@pytest.fixture()
def file_path(repo_root):
    return os.path.join(repo_root, 'files', '90x75_2.jpg')