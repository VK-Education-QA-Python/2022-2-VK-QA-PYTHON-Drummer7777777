import allure
import pytest
from ui.pages.create_company_page import CreateCompanyPage
from ui.locators.basic_locators import CompanyPageLocators
from ui.pages.main_page import MainPage


class CompanyPage(MainPage):
    urls = ['https://target-sandbox.my.com/dashboard', 'https://target-sandbox.my.com/dashboard#']

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    @allure.step('Click button create company')
    def create_company(self):
        self.click(CompanyPageLocators.BUTTON_CREATE_COMPANY_ON_MAIN)
        return CreateCompanyPage(self.driver)
