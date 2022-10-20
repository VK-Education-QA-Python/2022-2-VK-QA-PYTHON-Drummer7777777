import pytest
from ui.locators.basic_locators import Groups_OK_and_VK_pageLocators
from ui.pages.segments_page import SegmentsPage

class SegmentsGroups_OK_and_VK_Page(SegmentsPage):
    urls = ['https://target-sandbox.my.com/segments/groups_list']

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def add_name_group_in_row_search(self, text):
        self.input(Groups_OK_and_VK_pageLocators.ROW_SEARCH_GROUP, text)

    def select_group(self, text):
        self.click(Groups_OK_and_VK_pageLocators.BUTTON_SHOW)
        selector, path = (Groups_OK_and_VK_pageLocators.LIST_FOUND_GROUPS)
        self.click((selector, f"{path}/li[contains(@title, '{text}')]"))
        self.click(Groups_OK_and_VK_pageLocators.BUTTON_ADD_SELECTED)

    def delete_group(self, text):
        list_groups = self.driver.find_elements(*Groups_OK_and_VK_pageLocators.ROW_GROUP_IN_TABLE)
        locator, path = Groups_OK_and_VK_pageLocators.CELL_NAME_CURRENT_GROUP
        for group in list_groups:
            if group.find_element(locator, f"{path}/span").text == text:
                group.find_element(*Groups_OK_and_VK_pageLocators.BUTTON_DELETE_GROUP).click()
                group.find_element(*Groups_OK_and_VK_pageLocators.BUTTON_CONFIRM_DELETE).click()


