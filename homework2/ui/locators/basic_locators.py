from selenium.webdriver.common.by import By


class LoginPageLocators:
    AUTH_BUTTON = (By.XPATH, "//div[contains(@class,'responseHead-module-button-')]")
    AREA_EMAIL = (By.NAME, 'email')
    AREA_PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON_ON_FORM = (By.XPATH, "//div[contains(@class,'authForm-module-button-')]")


class MainPageLocators:
    PROFILE_MENU = (By.XPATH, "//a[contains(@class,'center-module-profile-')]")
    STATISTICS_MENU = (By.XPATH, "//a[contains(@class,'center-module-statistics-')]")
    COMPANY_MENU = (By.XPATH, "//a[contains(@class,'center-module-campaigns-')]")
    SEGMENTS_MENU = (By.XPATH, "//a[contains(@class,'center-module-segments-')]")
    SPINNER = (By.XPATH, "//div[contains(@class, 'spinner')]")


class SegmentsPageLocators:
    BUTTON_GROUPS_OK_AND_VK = (By.XPATH, "//a[contains(@href, '/segments/groups_list')]")
    BUTTON_SEGMENTS_LIST = (By.XPATH, "//a[contains(@href, '/segments/segments_list')]")


class SegmentsSegmentsListPageLocators:
    BUTTON_CREATE_PAGE = (By.XPATH, "//button[contains(@class, 'button_submit')]")
    CELLS = (By.XPATH, "//div[contains(@class, 'main-module-Cell-')]")
    CELL_EXIST_SEGMENT = (By.XPATH, "//div[contains(@class, 'cells-module-nameCell-')]/a")
    CELL_REMOVE_SEGMENT = (By.XPATH, "//div[contains(@data-test, 'remove')]/span")
    BUTTON_DELETE_SEGMENT = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")
    HORIZONTAL_SCROLL_TABLE_WITH_SEGMENTS = (By.XPATH, "//div[contains(@class, '_horizontal custom-scroll__handler-wrap')]")
    BUTTON_ACTIONS_WITH_TABLE = (By.XPATH, "//div[contains(@class, 'segmentsTable-module-massActionsSelect-')]")
    BUTTON_REMOVE_IN_ACTIONS = (By.XPATH, "/li[@data-id='remove']")


class CompanyPageLocators:
    HEAD_CONTROL = "//div[contains(@class, 'dashboard-module-headControlsWrapper-')]"
    BUTTON_CREATE_COMPANY_ON_MAIN = (By.XPATH, f"{HEAD_CONTROL}//div[contains(@data-test, 'button')]")
    CELL_EXIST_COMPANY = (By.XPATH, "//a[contains(@class, 'nameCell-module-campaignNameLink-')]")


class Groups_OK_and_VK_pageLocators:
    ROW_SEARCH_GROUP = (By.XPATH, "//input[contains(@class, '-searchInput-')]")
    BUTTON_SHOW = (By.XPATH, "//div[contains(@data-test, 'show')]")
    LIST_FOUND_GROUPS = (By.XPATH, "//ul[contains(@class, 'optionsList-module-list-')]")
    BUTTON_ADD_SELECTED = (By.XPATH, "//div[contains(@class, 'button-module-textWrapper-')]")
    BUTTON_DELETE_GROUP = (By.XPATH, "//span[contains(@class, 'icon-cross')]")
    BUTTON_CONFIRM_DELETE = (By.XPATH, "//button[contains(@class, 'button_confirm-remove')]")
    ROW_GROUP_IN_TABLE = (By.XPATH, "//tr[contains(@class, 'flexi-table__row')]")
    CELL_NAME_CURRENT_GROUP = (By.XPATH, "//td[contains(@class, 'js-cell-name')]")


class CreateCompanyLocators:
    TARGET_PRODUCTS_VK = (By.XPATH, "//div[contains(@cid, 'view743')]")
    ROW_ADD_URL = (By.XPATH, "//input[contains(@data-gtm-id, 'ad_url_text')]")
    COMMERCIAL_PRODUCT_TIZER_90x75 = (By.XPATH, "//div[contains(@class, 'pac-id-451')]")
    ROW_TITLE_BANNERS = (By.XPATH, "//input[contains(@data-name, 'title_25')]")
    ROW_DESCRIPTION_BANNERS = (By.XPATH, "//textarea[contains(@data-name, 'text_90')]")
    BUTTON_UPLOAD_IMAGE = (By.XPATH, "//div[contains(@class, 'roles-module-buttonWrap-')]/div[contains(@class, 'upload-module-wrapper-')]/input") # "/div[@data-test='button-upload']") #
    BUTTON_SAVE_IMAGE = (By.XPATH, "//input[contains(@class, 'image-cropper__save')]")
    BUTTON_SAVE_BANNER = (By.XPATH, "//div[contains(@data-test, 'submit_banner_button')]")
    ROW_COMPANY_NAME = (By.XPATH, "//div[contains(@class, 'input_campaign-name')]//input")
    BUTTON_SAVE_COMPANY = (By.XPATH, "//button[contains(@cid, 'view642')]")


class CreateSegmentLocators:
    SEGMENT_APPS_AND_GAMES = (By.XPATH, "//div[contains(@class, 'adding-segments-item') and"
                                        " (contains(text(), 'Приложения и игры в соцсетях') or"
                                        " contains(text(), 'Apps and games in social networks'))]")
    SEGMENT_GROUPS_OK_AND_VK = (By.XPATH, "//div[contains(@class, 'adding-segments-item') and"
                                        " (contains(text(), 'Группы ОК и VK') or"
                                        " contains(text(), 'Groups OK and VK'))]")
    CHECKBOX_PLAYED_AND_PAID_ON_THE_PLATFORM = (By.XPATH, "//input[contains(@class, 'adding-segments-source__checkbox')]")
    ROW_GROUP_IN_SEGMENT_GROUPS_OK_AND_VK = (By.XPATH, "//div[contains(@class, 'adding-segments-source__header')]")
    NAME_GROUP_IN_ROW_GROUP_IN_SEGMENT_GROUPS_OK_AND_VK = (By.XPATH, "//div[contains(@class, 'adding-segments-source__header')]/div/div/span")
    CHECKBOX_CURRENT_GROUP_IN_ROW_GROUP_IN_SEGMENT_GROUPS_OK_AND_VK = (By.XPATH, "//div[contains(@class, 'adding-segments-source__header')]//input")
    BUTTON_ADD_SEGMENT = (By.XPATH, "//div[contains(@class, 'js-add-button')]/button")
    ROW_NAME_SEGMENT = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]//input")
    BUTTON_CREATE_SEGMENT = (By.XPATH, "//button[contains(@data-class-name, 'Submit')]")
