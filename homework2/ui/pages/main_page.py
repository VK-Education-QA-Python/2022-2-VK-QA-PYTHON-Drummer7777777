import allure
import pytest
from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage
import time


class PageNotOpenedExeption(Exception):
    pass

class MainPage(BasePage):
    urls = ['https://target-sandbox.my.com/dashboard', 'https://target-sandbox.my.com/dashboard#']

    @allure.step('is_openned')
    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url in self.urls:
                return True
        raise PageNotOpenedExeption(f'URL:{self.driver.current_url}, expected {self.urls}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    @allure.step('go_to_profile')
    def go_to_profile(self):
        self.click(MainPageLocators.PROFILE_MENU)

    @allure.step('Go to page company')
    def go_to_company(self):
        self.click(MainPageLocators.COMPANY_MENU)
        from ui.pages.company_page import CompanyPage
        return CompanyPage(self.driver)

    @allure.step('return_company_page')
    def return_company_page(self):
        from ui.pages.company_page import CompanyPage
        return CompanyPage(self.driver)

    @allure.step('go_to_segments')
    def go_to_segments(self):
        self.click((MainPageLocators.SEGMENTS_MENU))
        from ui.pages.segments_segments_list_page import SegmentsSegmentsListPage
        return SegmentsSegmentsListPage(self.driver)

    @allure.step('find_list_exist_entity')
    def find_list_exist_entity(self, locator):
        exist_entity = self.driver.find_elements(*locator)
        text_exist_entity = list()
        for ex_ent in exist_entity:
            text_exist_entity.append(ex_ent.text)
        count_exist_entity = len(text_exist_entity)
        return text_exist_entity, count_exist_entity

    @allure.step('assert_exist_entity')
    def assert_exist_entity(self, text_exist_entity, count_exist_entity, name_entity):
        for ex_ent in range(count_exist_entity):
            if text_exist_entity[ex_ent] == f'{name_entity}':
                assert text_exist_entity[ex_ent] == f'{name_entity}'
                break
            elif ex_ent == count_exist_entity-1:
                pytest.fail()

