import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
def test_button_add_to_basket_is_visible(browser):

        # Открываем страницу товара
        browser.get(link)

        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(30)

        # Проверяем наличие кнопки добавления товара в корзину
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")