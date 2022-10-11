import pytest
import time
from base import BaseCase,Login
from ui.locators import basic_locators
import creds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



@pytest.mark.UI
class TestLogin(Login):
    def test_login(self):
        self.login()
        assert self.find(*basic_locators.AUTH_USER).get_attribute('data-ga-username') == creds.LOGIN


@pytest.mark.UI
class TestLoginInvalid(BaseCase):
    def test_login_invalid_mask_email(self):
        self.click(locator=basic_locators.AUTH_BUTTON)
        self.input(locator=basic_locators.AREA_EMAIL, text='asd')
        self.input(locator=basic_locators.AREA_PASSWORD, text=creds.PASSWORD)
        self.click(locator=basic_locators.LOGIN_BUTTON_ON_FORM)
        assert len(self.driver.find_elements(*basic_locators.AUTH_ERROR_LOGIN)) > 0

    def test_login_invalid_email_or_password(self):
        self.click(locator=basic_locators.AUTH_BUTTON)
        self.input(locator=basic_locators.AREA_EMAIL, text='test@gmail.com')
        self.input(locator=basic_locators.AREA_PASSWORD, text='asd')
        self.click(locator=basic_locators.LOGIN_BUTTON_ON_FORM)
        assert len(self.driver.find_elements(*basic_locators.AUTH_ERROR_EMAIL_OR_PASSWORD)) > 0


@pytest.mark.UI
class TestLogout(Login):
    def test_logout(self):
        self.login()
        if self.find(*basic_locators.PAGE_BODY):
            WebDriverWait(self.driver,5).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".js-page-header")))
            self.click(locator=basic_locators.USER_NAME_WRAP)
            element = self.find(*basic_locators.USER_NAME_WRAP_LOGOUT)
            time.sleep(1)
            if element.is_displayed():
                action = ActionChains(self.driver)
                action.click(on_element=element)
                action.perform()
            assert len(self.driver.find_elements(*basic_locators.AUTH_BUTTON)) > 0


@pytest.mark.UI
class TestEditContactInfoInProfile(Login):
    def test_edit(self):
        self.login()
        self.click(locator=basic_locators.PROFILE_MENU)
        self.input(locator=basic_locators.PROFILE_MENU_ROW_FIO,text='FIO')
        self.input(locator=basic_locators.PROFILE_MENU_ROW_INN,text='123456789012')
        self.input(locator=basic_locators.PROFILE_MENU_ROW_PHONE,text='+79993331212')
        self.click(locator=basic_locators.PROFILE_MENU_SAVE)
        assert len(self.driver.find_elements(*basic_locators.PROFILE_MENU_NOTIFI_DATA_SAVE)) > 0

@pytest.mark.UI
class TestMenuButton(Login):
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            (basic_locators.PROFILE_MENU, 'page_profile'),
            (basic_locators.STATISTICS_MENU, 'page_statistics')
        ]
    )
    def test_moving(self,test_input,expected):
        self.login()
        self.click(locator=test_input)
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element((By.CSS_SELECTOR, ".spinner")))
        assert expected in self.find(*basic_locators.NAME_PAGE).get_attribute('class')


