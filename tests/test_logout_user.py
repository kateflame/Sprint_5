import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators import *


class TestLogoutUser:
    def test_logout_user(self, driver, driver_with_exists_account):

        # Нажать на кнопку Выйти
        driver.find_element(*BUTTON_EXIT).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(REGISTRATION_BUTTON)
        )

        registration = driver.find_element(*REGISTRATION_BUTTON)
        user_elements = driver.find_elements(*USER_NAME_LOCATOR)
        user_avater = driver.find_elements(*USER_AVATAR_LOCATOR)

        assert (
            registration.text == "Вход и регистрация"
            and len(user_elements) == 0
            and len(user_avater) == 0
        )
