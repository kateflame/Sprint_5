import pytest
from ..locators import *
from ..urls import login_page


class TestLoginAccount:
    def test_login(self, driver, driver_with_exists_account):

        user_name = driver.find_element(*USER_NAME_LOCATOR)

        user_avater = driver.find_element(*USER_AVATAR_LOCATOR)
        # Проверить: произошёл переход на главную страницу, отображается аватар пользователя и имя User.
        assert (
            driver.current_url == login_page
            and user_name.text == "User."
            and user_avater.is_displayed()
        )
