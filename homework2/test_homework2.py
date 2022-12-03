import allure
import pytest
from base import BaseCase
from ui.locators.basic_locators import CompanyPageLocators
from ui.locators.basic_locators import SegmentsSegmentsListPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestLogin(BaseCase):
    # @pytest.mark.skip
    @pytest.mark.UI
    @allure.step('Test_create_company')
    def test_create_company(self, file_path):
        self.logger.info('Start')
        from ui.pages.main_page import MainPage
        main_page = MainPage(self.driver)
        self.logger.info('Go to page company')
        company_page = main_page.go_to_company()
        self.logger.info('Wait spinner')
        company_page.wait_load_spinner()
        self.logger.info('Click button create company')
        create_company_page = company_page.create_company()
        self.logger.info('Wait spinner')
        create_company_page.wait_load_spinner()
        self.logger.info('Select target products')
        create_company_page.select_target_products_vk()
        self.logger.info('Input url')
        create_company_page.input_url_commercial_target(url='https://target-sandbox.my.com')
        self.logger.info('Select product')
        create_company_page.select_commercial_product_tizer_90x75()
        self.logger.info('Add banner')
        create_company_page.add_banner(file_path)
        self.logger.info('Add name company')
        name_company = create_company_page.add_name_company()
        self.logger.info('Click button create company')
        company_page = create_company_page.create_company()
        self.logger.info('Wait cell with name in table')
        WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH, "//a[contains(@class, 'nameCell-module-campaignNameLink-')]")))
        self.logger.info('Load exist name company from table')
        text_exist_company, count_exist_company = company_page.find_list_exist_entity(CompanyPageLocators.CELL_EXIST_COMPANY)
        self.logger.info('Assert created company')
        company_page.assert_exist_entity(text_exist_company, count_exist_company, name_company)

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_create_segment(self):
        from ui.pages.main_page import MainPage
        main_page = MainPage(self.driver)
        self.logger.info('Go to page segments')
        segment_segments_list_page = main_page.go_to_segments()
        self.logger.info('Click button create segment')
        create_segment_page = segment_segments_list_page.creat_segment()
        self.logger.info('Select apps and games')
        create_segment_page.select_apps_and_games()
        self.logger.info('On checkbox playes and paid')
        create_segment_page.on_checkbox_played_and_paid_on_the_platform()
        self.logger.info('Click button add')
        create_segment_page.add_segment()
        self.logger.info('Add name segment')
        name_segment = create_segment_page.add_name_segment()
        self.logger.info('Click button create')
        segment_segments_list_page = create_segment_page.create_segment()
        self.logger.info('Load exist name segment from table')
        text_exist_segment, count_exist_segment = segment_segments_list_page.find_list_exist_entity(SegmentsSegmentsListPageLocators.CELL_EXIST_SEGMENT)
        self.logger.info('Assert created segment')
        segment_segments_list_page.assert_exist_entity(text_exist_segment, count_exist_segment, name_segment)

    # @pytest.mark.skip
    @pytest.mark.UI
    def test_create_segment_with_VK_group(self):
        from ui.pages.main_page import MainPage
        main_page = MainPage(self.driver)
        self.logger.info('Go to page segments')
        segments_segments_list_page = main_page.go_to_segments()
        self.logger.info('Go to groups OK and VK')
        segments_ok_vk_page = segments_segments_list_page.go_to_groups_OK_and_VK()
        group = 'VK Образование' #'Group VK «VK Образование»#97268017 people'
        self.logger.info('Add name group in row search')
        segments_ok_vk_page.add_name_group_in_row_search(group)
        self.logger.info('Select current group in found list')
        segments_ok_vk_page.select_group(group)
        self.logger.info('Go to segments list')
        segments_segments_list_page = segments_ok_vk_page.go_to_segments_list()
        self.logger.info('Click button create segment')
        create_segment_page = segments_segments_list_page.creat_segment()
        self.logger.info('Select groups OK and VK')
        create_segment_page.select_groups_OK_and_VK()
        self.logger.info('On checkbox current group')
        create_segment_page.on_checkbox_current_group(group)
        self.logger.info('Click button add')
        create_segment_page.add_segment()
        self.logger.info('Add name segment')
        name_segment = create_segment_page.add_name_segment()
        self.logger.info('Click button create')
        segments_segments_list_page = create_segment_page.create_segment()
        self.logger.info('Load exist name segment from table')
        text_exist_segment, count_exist_segment = segments_segments_list_page.find_list_exist_entity(
            SegmentsSegmentsListPageLocators.CELL_EXIST_SEGMENT)
        self.logger.info('Assert created segment')
        segments_segments_list_page.assert_exist_entity(text_exist_segment, count_exist_segment, name_segment)
        self.logger.info('Delete created segment')
        segments_segments_list_page.delete_segment(name_segment)
        self.logger.info('Go to groups OK and VK')
        segments_ok_vk_page = segments_segments_list_page.go_to_groups_OK_and_VK()
        self.logger.info('Delete created group')
        segments_ok_vk_page.delete_group(group)
