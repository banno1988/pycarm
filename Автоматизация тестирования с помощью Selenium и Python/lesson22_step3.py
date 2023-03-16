from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#num1')
    print(x.text)
    y = browser.find_element(By.CSS_SELECTOR, '#num2')
    z=int(x.text)+int(y.text)
    print(z)
    browser.find_element(By.CSS_SELECTOR, "select.custom-select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{str(z)}']").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла