import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.basic_locators import MainPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Wait element located')
    def wait_for_search(self, by, what):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((by, what)))

    @allure.step('Find element')
    def find(self, by, what, timeout=5):
        self.wait_for_search(by, what)
        return self.driver.find_element(by, what)

    @allure.step('Input text')
    def input(self, locator, text):
        elem = self.find(*locator)
        elem.clear()
        elem.send_keys(text)

    @allure.step('Wait element clickable')
    def wait(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Click button')
    def click(self, locator):
        self.find(*locator)
        elem = self.wait(locator)
        elem.click()

    @allure.step('Wait load spinner')
    def wait_load_spinner(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(MainPageLocators.SPINNER))
