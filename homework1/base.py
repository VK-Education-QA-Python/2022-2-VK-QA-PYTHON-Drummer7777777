import pytest
from ui.locators import basic_locators
import creds


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, by, what):
        return self.driver.find_element(by, what)

    def input(self, locator, text):
        elem = self.find(*locator)
        elem.clear()
        elem.send_keys(text)

    def click(self, locator):
        elem = self.find(*locator)
        elem.click()
        return

class Login(BaseCase):
    def login(self):
        self.click(locator=basic_locators.AUTH_BUTTON)
        self.input(locator=basic_locators.AREA_EMAIL, text=creds.LOGIN)
        self.input(locator=basic_locators.AREA_PASSWORD, text=creds.PASSWORD)
        self.click(locator=basic_locators.LOGIN_BUTTON_ON_FORM)
