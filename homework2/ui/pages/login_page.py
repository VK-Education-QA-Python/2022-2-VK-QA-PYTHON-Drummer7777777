import pytest
from ui.locators.basic_locators import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, user, password):
        self.click(locator=LoginPageLocators.AUTH_BUTTON)
        self.input(locator=LoginPageLocators.AREA_EMAIL, text=user)
        self.input(locator=LoginPageLocators.AREA_PASSWORD, text=password)
        self.click(locator=LoginPageLocators.LOGIN_BUTTON_ON_FORM)
