import allure

from ui.locators.basic_locators import CreateSegmentLocators
import time
from ui.pages.main_page import MainPage


class CreateSegmentPage(MainPage):
    urls = ['https://target-sandbox.my.com/segments/segments_list/new']

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    @allure.step('select_apps_and_games')
    def select_apps_and_games(self):
        self.click(CreateSegmentLocators.SEGMENT_APPS_AND_GAMES)

    @allure.step('select_groups_OK_and_VK')
    def select_groups_OK_and_VK(self):
        self.click(CreateSegmentLocators.SEGMENT_GROUPS_OK_AND_VK)

    @allure.step('on_checkbox_played_and_paid_on_the_platform')
    def on_checkbox_played_and_paid_on_the_platform(self):
        checkbox = self.find(*CreateSegmentLocators.CHECKBOX_PLAYED_AND_PAID_ON_THE_PLATFORM)
        if checkbox.is_selected() == False:
            checkbox.click()

    @allure.step('on_checkbox_current_group')
    def on_checkbox_current_group(self, text):
        groups = self.driver.find_elements(*CreateSegmentLocators.ROW_GROUP_IN_SEGMENT_GROUPS_OK_AND_VK)
        for group in groups:
            if text in group.find_element(*CreateSegmentLocators.NAME_GROUP_IN_ROW_GROUP_IN_SEGMENT_GROUPS_OK_AND_VK).text:
                checkbox = group.find_element(*CreateSegmentLocators.CHECKBOX_CURRENT_GROUP_IN_ROW_GROUP_IN_SEGMENT_GROUPS_OK_AND_VK)
                if checkbox.is_selected() == False:
                    checkbox.click()
                time.sleep(5)
                break

    @allure.step('add_segment')
    def add_segment(self):
        self.click(CreateSegmentLocators.BUTTON_ADD_SEGMENT)

    @allure.step('add_name_segment')
    def add_name_segment(self, name=f'TEST SEGMENT {time.time()}'):
        self.input(CreateSegmentLocators.ROW_NAME_SEGMENT, name)
        return name

    @allure.step('create_segment')
    def create_segment(self):
        self.click(CreateSegmentLocators.BUTTON_CREATE_SEGMENT)
        from ui.pages.segments_segments_list_page import SegmentsSegmentsListPage
        return SegmentsSegmentsListPage(self.driver)
        time.sleep(5)

