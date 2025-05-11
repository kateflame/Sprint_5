import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ..locators import *


@pytest.mark.usefixtures("driver")
class TestCreateAdNonehAuth:
    def test_create_ad_without_avthorization(self, driver):
        # Нажать на кнопку Разместить объявление
        driver.find_element(*BUTTON_ADD).click()

        # Добавила явное ожидание открытия модального окна
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MODAL_TITLE)
        )

        title_name = driver.find_element(*MODAL_TITLE_TEXT)
        # проверка на отображаение модального окна с заголовком «Чтобы разместить объявление, авторизуйтесь
        assert title_name.text == "Чтобы разместить объявление, авторизуйтесь"
