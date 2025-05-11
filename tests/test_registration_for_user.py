from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from ..locators import *
from .data import *


def test_register(driver_regist_new_account):

    driver_regist_new_account.find_element(*EMAIL).send_keys(user_name_new_user)

    driver_regist_new_account.find_element(*PASSWORD).send_keys(password_new_user)

    driver_regist_new_account.find_element(*SUBMIT_PASSWORD).send_keys(
        password_new_user
    )

    driver_regist_new_account.find_element(*CREATE_ACCOUN_BUTTON).click()

    # Добавь явное ожидание для загрузки кнопки выйти на странице
    WebDriverWait(driver_regist_new_account, 5).until(
        expected_conditions.visibility_of_element_located(BUTTON_EXIT)
    )

    user_name = driver_regist_new_account.find_element(*USER_NAME_LOCATOR)

    user_avater = driver_regist_new_account.find_element(*USER_AVATAR_LOCATOR)
    # Проверить: произошёл переход на главную страницу, отображается аватар пользователя и имя User.
    assert (
        driver_regist_new_account.current_url
        == "https://qa-desk.stand.praktikum-services.ru/regiatration"
        and user_name.text == "User."
        and user_avater.is_displayed()
    )

    driver_regist_new_account.quit()
