from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


REGISTRATION_BUTTON = (
    By.XPATH,
    "//*[@class='header_shell__zlCGj']/div/button[@class ='buttonSecondary inButtonText undefined inButtonText']",
)
DONT_HAVE_ACCOUNT_BUTTON = (
    By.XPATH,
    "//*[@id='root']/div/div[2]/div/form/div[3]/button[2]",
)

CREATE_ACCOUN_BUTTON = (By.XPATH, "//div[@class ='popUp_buttonRow__+W8JD']/button[1]")
USER_NAME_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/h3')
MODAL_WINDOW_ENTER_LOCATOR = (By.CLASS_NAME, "homePage_modal__zSdUB")
BUTTON_EXIT = (By.XPATH, '//*[@class ="header_flexRow__Xdqv1"]/div/div/button')
PASSWORD = (By.NAME, "password")
SUBMIT_PASSWORD = (By.NAME, "submitPassword")
EMAIL = (By.NAME, "email")
USER_AVATAR_LOCATOR = (By.CSS_SELECTOR, ".circleSmall > svg")
ERROR_LOCATOR = (By.CSS_SELECTOR, ".input_span__yWPqB")
INPUT_ERROR = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
BUTTON_ENTER = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]')
BUTTON_APPLY = (By.XPATH, "//form/div[2]/button")
BUTTON_ADD = (
    By.XPATH,
    "//*[@class='header_shell__zlCGj']/div/button[@class ='buttonPrimary inButtonText undefined inButtonText']",
)
MODAL_TITLE = (By.CLASS_NAME, "popUp_titleRow__M7tGg")
MODAL_TITLE_TEXT = (
    By.XPATH,
    "//form[@class='popUp_shell__LuyqR']/div[@class='popUp_titleRow__M7tGg']/h1",
)
SUBMIT_BUTTON = (
    By.XPATH,
    "//form/button[@class='buttonPrimary inButtonText undefined inButtonText']",
)
NAME_FOR_PRODUCT_INPUT = (
    By.NAME,
    "name",
)
PRODUCT_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
PRICE_INPUT = (
    By.NAME,
    "price",
)

RADIO_BUTTON = (By.XPATH, "//form/fieldset/div/div[2]/div")

DROPDOWN_CATEGORY = (By.XPATH, "//form/div[2]/div[2]/div[1]/button")
DROPDOWN_CATEGORY_GARDEN = (
    By.XPATH,
    "//form/div[2]/div[2]/div[2]/button[3]",
)

DROPDOWN_CITY = (By.XPATH, "//form/div[3]/div[1]/button")

DROPDOWN_CITY_EKATERINBURG = (By.XPATH, "//form/div[3]/div[2]/button[4]")
PROFILE_BUTTON = (By.CSS_SELECTOR, ".circleSmall")


def getProductsCard(name):
    return (By.XPATH, f"//img[contains(@alt, '{name}')]")


WANT_BUY_INPUT = (By.XPATH, "/html/body/div/div/div[2]/form/div[1]/div/div/input")
PROFILE_CARD_LIST_TITLE = (
    By.XPATH,
    '//*[@id="root"]/div/div[2]/div[4]/div/div[1]/div[1]',
)
