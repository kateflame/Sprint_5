from ..locators import *


def test_register_exists_account(driver_with_exists_account):

    user_name = driver_with_exists_account.find_element(*USER_NAME_LOCATOR)

    user_avater = driver_with_exists_account.find_element(*USER_AVATAR_LOCATOR)
    # Проверить: произошёл переход на главную страницу, отображается аватар пользователя и имя User.
    assert (
        driver_with_exists_account.current_url
        == "https://qa-desk.stand.praktikum-services.ru/login"
        and user_name.text == "User."
        and user_avater.is_displayed()
    )

    driver_with_exists_account.quit()
