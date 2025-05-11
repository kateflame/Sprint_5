import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators import *
import random


class TestCreateAdWithAuth:
    def test_create_ad(self, driver, driver_with_exists_account):

        driver.find_element(*BUTTON_ADD).click()

        # Добавила явное ожидание открытия модального окна
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(SUBMIT_BUTTON)
        )

        # Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
        product_name = f"Тостер{random.randint(100,999)}"

        description = "Продаю тостер в отличном состоянии"

        price = random.randint(7000, 9999)

        driver.find_element(*NAME_FOR_PRODUCT_INPUT).send_keys(product_name)
        driver.find_element(*PRODUCT_DESCRIPTION).send_keys(description)
        driver.find_element(*PRICE_INPUT).send_keys(price)

        # Выбрать из Dropdown «Категорию» и Садоводство.
        driver.find_element(*DROPDOWN_CATEGORY).click()
        driver.find_element(*DROPDOWN_CATEGORY_GARDEN).click()
        # Выбрать из Dropdown «Город и Екатеринбург.
        driver.find_element(*DROPDOWN_CITY).click()
        driver.find_element(*DROPDOWN_CITY_EKATERINBURG).click()

        # Выбрать RabioButton «Состояние товара» Б/У
        driver.find_element(*RADIO_BUTTON).click()
        # Нажать кнопку опубликовать
        driver.find_element(*SUBMIT_BUTTON).click()
        # Добавила явное ожидание открытия ввода строки Хочу купить

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(WANT_BUY_INPUT)
        )

        # Перейти в профиль пользователя.
        driver.find_element(*PROFILE_BUTTON).click()
        # Добавила явное ожидание загркзки карточек объявлений

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(PROFILE_CARD_LIST_TITLE)
        )

        card = driver.find_element(*getProductsCard(product_name))

        assert card.is_displayed()
