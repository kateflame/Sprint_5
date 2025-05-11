import pytest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators import *
from ..data import login_name_for_authorize_user, password_for_authorize_user
from ..urls import main_page


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(main_page)
    return driver


@pytest.fixture
def driver_with_exists_account(driver):
    # Кликнуть на кнопку вход и регистрация
    driver.find_element(*REGISTRATION_BUTTON).click()
    # Добавила явное ожидание
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(MODAL_WINDOW_ENTER_LOCATOR)
    )
    # ввести email, password, submitpassword по существующему пользователю
    driver.find_element(*EMAIL).send_keys(login_name_for_authorize_user)
    driver.find_element(*PASSWORD).send_keys(password_for_authorize_user)

    # нажать на кнопку Войти
    driver.find_element(*BUTTON_ENTER).click()

    # Добавила явное ожидание кнопки выйти на странице
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(BUTTON_EXIT)
    )


@pytest.fixture
def driver_regist_new_account(driver):
    driver.find_element(*REGISTRATION_BUTTON).click()

    # Добавь явное ожидание
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(MODAL_WINDOW_ENTER_LOCATOR)
    )
    # кликнуть по кнопке Нет аккаунта
    driver.find_element(*DONT_HAVE_ACCOUNT_BUTTON).click()

    # Добавь явное ожидание
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((MODAL_WINDOW_ENTER_LOCATOR))
    )
