import allure
import pytest
from ui.locators.basic_locators import SegmentsSegmentsListPageLocators
from ui.pages.create_segment_page import CreateSegmentPage
from ui.pages.segments_page import SegmentsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SegmentsSegmentsListPage(SegmentsPage):
    urls = ['https://target-sandbox.my.com/segments/segments_list']

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    @allure.step('creat_segment')
    def creat_segment(self):
        self.click(SegmentsSegmentsListPageLocators.BUTTON_CREATE_PAGE)
        return CreateSegmentPage(self.driver)

    @allure.step('delete_segment')
    def delete_segment(self, name_segment):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((SegmentsSegmentsListPageLocators.CELLS)))
        cells = self.driver.find_elements(*SegmentsSegmentsListPageLocators.CELLS)
        find = True
        locator, path = SegmentsSegmentsListPageLocators.CELLS
        for cell in cells:
            cell_text = cell.find_element(locator, f'{path}/div/a').text
            if cell_text == name_segment and find == True:
                id_segment = cell.get_attribute('data-test').split('-')[2]
                find = False
            if find == False:
                # break
                if cell.get_attribute('data-test') == f'remove-{id_segment} row-{id_segment}':
                    cell.find_element(locator, f'{path}/span').click()
                    break
        # from selenium.webdriver.common.by import By
        # checkbox = self.find(By.XPATH, f"//div[contains(@data-test, 'id-{id_segment} row-{id_segment}')]/div/input")
        # if checkbox.is_selected() == False:
        #     checkbox.click()
        # self.click(SegmentsSegmentsListPageLocators.BUTTON_ACTIONS_WITH_TABLE)
        # self.click(SegmentsSegmentsListPageLocators.BUTTON_REMOVE_IN_ACTIONS)

        self.click(SegmentsSegmentsListPageLocators.BUTTON_DELETE_SEGMENT)


