from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators import *


def test_register_exists_account(driver_with_exists_account):

    # Нажать на кнопку Выйти
    driver_with_exists_account.find_element(*BUTTON_EXIT).click()

    WebDriverWait(driver_with_exists_account, 5).until(
        expected_conditions.visibility_of_element_located(REGISTRATION_BUTTON)
    )

    registration = driver_with_exists_account.find_element(*REGISTRATION_BUTTON)
    user_elements = driver_with_exists_account.find_elements(*USER_NAME_LOCATOR)
    user_avater = driver_with_exists_account.find_elements(*USER_AVATAR_LOCATOR)

    assert (
        registration.text == "Вход и регистрация"
        and len(user_elements) == 0
        and len(user_avater) == 0
    )

    driver_with_exists_account.quit()
