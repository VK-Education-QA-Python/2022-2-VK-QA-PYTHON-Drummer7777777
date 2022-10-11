from selenium.webdriver.common.by import By

#GENERAL
PAGE_BODY = (By.XPATH, "//div[contains(@class,'layout-module-pageBody-')]")
AUTH_USER = (By.XPATH, "//html")
NAME_PAGE = (By.XPATH, "//div[contains(@class,'page')]")

#AUTH_FORM
AUTH_BUTTON = (By.XPATH, "//div[contains(@class,'responseHead-module-button-')]")
AREA_EMAIL = (By.NAME, 'email')
AREA_PASSWORD = (By.NAME, 'password')
LOGIN_BUTTON_ON_FORM = (By.XPATH, "//div[contains(@class,'authForm-module-button-')]")

#AUTH_ERRORS
AUTH_ERROR_LOGIN = (By.XPATH, "//div[contains(@class,'notify-module-error-')]")
AUTH_ERROR_EMAIL_OR_PASSWORD = (By.XPATH, "//div[contains(@class,'js_form_msg')]")

#USER_NAME_WRAP
USER_NAME_WRAP = (By.XPATH,"//div[contains(@class,'right-module-userNameWrap-')]")
USER_NAME_WRAP_LOGOUT = (By.CSS_SELECTOR, "[href='/logout']")

#MENU_BUTTONS
PROFILE_MENU = (By.XPATH, "//a[contains(@class,'center-module-profile-')]")
STATISTICS_MENU = (By.XPATH, "//a[contains(@class,'center-module-statistics-')]")

#PROFILE_EDIT
PROFILE_MENU_ROW_FIO = (By.XPATH, "//div[contains(@data-name,'fio')]/div/input")
PROFILE_MENU_ROW_INN = (By.XPATH, "//div[contains(@data-name,'ordInn')]/div/input")
PROFILE_MENU_ROW_PHONE = (By.XPATH, "//div[contains(@data-name,'phone')]/div/input")
PROFILE_MENU_SAVE = (By.XPATH, "//button")
PROFILE_MENU_NOTIFI_DATA_SAVE = (By.XPATH, "//div[contains(@data-class-name,'SuccessView')]")
