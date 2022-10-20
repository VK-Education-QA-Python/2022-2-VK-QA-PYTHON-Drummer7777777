import os.path

import allure
import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write((f"{i['level']} - {i['source']}\n{i['message']}\n"))
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            self.driver.save_screenshot(filename=screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'browser.log', allure.attachment_type.TEXT)
            test_log = os.path.join(temp_dir, 'test.log')
            with open(test_log, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest, cookies):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.logger = logger

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
