import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from ..locators import *
from ..data import *


class TestUncorrectMask:
    def test_register_with_uncorrect_masks(self, driver, driver_regist_new_account):
        # ввести email, password, submitpassword
        driver.find_element(*EMAIL).send_keys(login_with_uncorrect_mask)

        driver.find_element(*PASSWORD).send_keys(password_new_user)

        driver.find_element(*SUBMIT_PASSWORD).send_keys(password_new_user)
        # нажать на кнопку Создать аккаунт
        driver.find_element(*CREATE_ACCOUN_BUTTON).click()
        # Добавь явное ожидание для загрузки текста ошибки под полем email
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(ERROR_LOCATOR)
        )
        # найти все поля  которые подсвечиватся красным и имею class name ='input_inputError__fLUP9'
        elements = driver.find_elements(*INPUT_ERROR)
        # проверка поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        error = driver.find_element(*ERROR_LOCATOR)
        assert error.text == "Ошибка" and len(elements) == 3
