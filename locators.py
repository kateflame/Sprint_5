from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


REGISTRATION_BUTTON = (
    By.XPATH,
    "//*[@class='header_shell__zlCGj']/div/button[@class ='buttonSecondary inButtonText undefined inButtonText']",
)
DONT_HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")

CREATE_ACCOUN_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
USER_NAME_LOCATOR = (By.CSS_SELECTOR, ".profileText")
MODAL_WINDOW_ENTER_LOCATOR = (By.CLASS_NAME, "homePage_modal__zSdUB")
BUTTON_EXIT = (By.XPATH, "//button[contains(text(), 'Выйти')]")
PASSWORD = (By.NAME, "password")
SUBMIT_PASSWORD = (By.NAME, "submitPassword")
EMAIL = (By.NAME, "email")
USER_AVATAR_LOCATOR = (By.CSS_SELECTOR, ".circleSmall > svg")
ERROR_LOCATOR = (By.CSS_SELECTOR, ".input_span__yWPqB")
INPUT_ERROR = (By.CSS_SELECTOR, ".input_inputError__fLUP9")
BUTTON_ENTER = (By.XPATH, "//button[contains(text(), 'Войти')]")
BUTTON_ADD = (
    By.XPATH,
    "//button[contains(text(), 'Разместить объявление')]",
)
MODAL_TITLE = (By.CLASS_NAME, "popUp_titleRow__M7tGg")
MODAL_TITLE_TEXT = (
    By.XPATH,
    "//div[@class='popUp_titleRow__M7tGg']/h1",
)
SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
NAME_FOR_PRODUCT_INPUT = (
    By.NAME,
    "name",
)
PRODUCT_DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
PRICE_INPUT = (
    By.NAME,
    "price",
)

RADIO_BUTTON = (By.CSS_SELECTOR, ".radioUnput_inputRegular__FbVbr")

DROPDOWN_CATEGORY = (By.XPATH, "//input[@name='category']/following-sibling::button")
DROPDOWN_CATEGORY_GARDEN = (
    By.XPATH,
    "//button//span[text()='Садоводство']/parent::button",
)

DROPDOWN_CITY = (By.XPATH, "//input[@name='city']/following-sibling::button")

DROPDOWN_CITY_EKATERINBURG = (
    By.XPATH,
    "//button//span[text()='Екатеринбург']/parent::button",
)
PROFILE_BUTTON = (By.CSS_SELECTOR, ".circleSmall")


def getProductsCard(name):
    return (By.XPATH, f"//img[contains(@alt, '{name}')]")


WANT_BUY_INPUT = (By.XPATH, "//input[@placeholder='Я хочу купить...']")
PROFILE_CARD_LIST_TITLE = (By.XPATH, "//div[contains(@class, 'card')]//h2")
