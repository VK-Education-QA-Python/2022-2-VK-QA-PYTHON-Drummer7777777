import allure
import pytest
from ui.locators.basic_locators import SegmentsPageLocators
from ui.pages.main_page import MainPage


class SegmentsPage(MainPage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('go_to_groups_OK_and_VK')
    def go_to_groups_OK_and_VK(self):
        self.click(SegmentsPageLocators.BUTTON_GROUPS_OK_AND_VK)
        from ui.pages.groups_OK_and_VK_page import SegmentsGroups_OK_and_VK_Page
        return SegmentsGroups_OK_and_VK_Page(self.driver)

    @allure.step('go_to_segments_list')
    def go_to_segments_list(self):
        self.click(SegmentsPageLocators.BUTTON_SEGMENTS_LIST)
        from ui.pages.segments_segments_list_page import SegmentsSegmentsListPage
        return SegmentsSegmentsListPage(self.driver)