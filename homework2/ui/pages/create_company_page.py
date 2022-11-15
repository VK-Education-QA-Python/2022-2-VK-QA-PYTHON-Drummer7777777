import allure

from ui.locators.basic_locators import CreateCompanyLocators
import time
from ui.pages.main_page import MainPage


class CreateCompanyPage(MainPage):
    urls = ['https://target-sandbox.my.com/campaign/new']

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    @allure.step('Select_target_products_vk')
    def select_target_products_vk(self):
        self.click(locator=CreateCompanyLocators.TARGET_PRODUCTS_VK)

    @allure.step('Input_url_commercial_target')
    def input_url_commercial_target(self, url):
        self.input(locator=CreateCompanyLocators.ROW_ADD_URL, text=url)

    @allure.step('Select_commercial_product_tizer_90x75')
    def select_commercial_product_tizer_90x75(self):
        self.click(locator=CreateCompanyLocators.COMMERCIAL_PRODUCT_TIZER_90x75)

    @allure.step('create_company')
    def create_company(self):
        self.click(locator=CreateCompanyLocators.BUTTON_SAVE_COMPANY)
        from ui.pages.company_page import CompanyPage
        return CompanyPage(self.driver)

    @allure.step('input_text_in_banner')
    def input_text_in_banner(self,title='Title',desccription='Description'):
        self.input(locator=CreateCompanyLocators.ROW_TITLE_BANNERS, text='Title')
        self.input(locator=CreateCompanyLocators.ROW_DESCRIPTION_BANNERS, text='Description')

    @allure.step('add_image')
    def add_image(self,file_path):
        self.find(*CreateCompanyLocators.BUTTON_UPLOAD_IMAGE).send_keys(file_path)
        self.click(locator=CreateCompanyLocators.BUTTON_SAVE_IMAGE)

    @allure.step('add_banne')
    def add_banner(self,file_path):
        self.input_text_in_banner()
        self.add_image(file_path)
        self.click(locator=CreateCompanyLocators.BUTTON_SAVE_BANNER)

    @allure.step('add_name_company')
    def add_name_company(self,name=f'TEST COMPANY {time.time()}'):
        name_company = name
        self.input(locator=CreateCompanyLocators.ROW_COMPANY_NAME, text=f'{name_company}')
        return name_company