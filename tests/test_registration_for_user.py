import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from ..locators import *
from ..data import *
from ..urls import register_page


class TestRegistrationAccount:
    def test_register(self, driver, driver_regist_new_account):

        driver.find_element(*EMAIL).send_keys(user_name_new_user)

        driver.find_element(*PASSWORD).send_keys(password_new_user)

        driver.find_element(*SUBMIT_PASSWORD).send_keys(password_new_user)

        driver.find_element(*CREATE_ACCOUN_BUTTON).click()

        # Добавь явное ожидание для загрузки кнопки выйти на странице
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BUTTON_EXIT)
        )

        user_name = driver.find_element(*USER_NAME_LOCATOR)

        user_avater = driver.find_element(*USER_AVATAR_LOCATOR)
        # Проверить: произошёл переход на страницу регистрации, отображается аватар пользователя и имя User.
        assert (
            driver.current_url == register_page
            and user_name.text == "User."
            and user_avater.is_displayed()
        )
