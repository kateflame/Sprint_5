from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators import *
import random
import time


def test_register_exists_account(driver_with_exists_account):

    driver_with_exists_account.find_element(*BUTTON_ADD).click()

    # Добавила явное ожидание открытия модального окна
    WebDriverWait(driver_with_exists_account, 3).until(
        expected_conditions.visibility_of_element_located(SUBMIT_BUTTON)
    )

    # Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
    product_name = f"Тостер{random.randint(100,999)}"

    description = "Продаю тостер в отличном состоянии"

    price = random.randint(7000, 9999)

    driver_with_exists_account.find_element(*NAME_FOR_PRODUCT_INPUT).send_keys(
        product_name
    )
    driver_with_exists_account.find_element(*PRODUCT_DESCRIPTION).send_keys(description)
    driver_with_exists_account.find_element(*PRICE_INPUT).send_keys(price)

    # Выбрать из Dropdown «Категорию» и Садоводство.
    driver_with_exists_account.find_element(*DROPDOWN_CATEGORY).click()
    driver_with_exists_account.find_element(*DROPDOWN_CATEGORY_GARDEN).click()
    # Выбрать из Dropdown «Город и Екатеринбург.
    driver_with_exists_account.find_element(*DROPDOWN_CITY).click()
    driver_with_exists_account.find_element(*DROPDOWN_CITY_EKATERINBURG).click()

    # Выбрать RabioButton «Состояние товара» Б/У
    driver_with_exists_account.find_element(*RADIO_BUTTON).click()
    # Нажать кнопку опубликовать
    driver_with_exists_account.find_element(*SUBMIT_BUTTON).click()
    # Добавила явное ожидание открытия ввода строки Хочу купить

    WebDriverWait(driver_with_exists_account, 3).until(
        expected_conditions.visibility_of_element_located(WANT_BUY_INPUT)
    )

    # Перейти в профиль пользователя.
    driver_with_exists_account.find_element(*PROFILE_BUTTON).click()
    # Добавила явное ожидание загркзки карточек объявлений

    WebDriverWait(driver_with_exists_account, 3).until(
        expected_conditions.visibility_of_element_located(PROFILE_CARD_LIST_TITLE)
    )

    card = driver_with_exists_account.find_element(*getProductsCard(product_name))

    assert card.is_displayed()

    driver_with_exists_account.quit()
