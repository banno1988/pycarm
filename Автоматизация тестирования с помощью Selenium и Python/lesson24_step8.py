from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    #browser.implicitly_wait(12)
    browser.get(link)

    waiter = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
        )
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


    x_element = WebDriverWait(browser,12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input_value"))
        )
    x = x_element.text
    y = calc(x)

    input1 = WebDriverWait(browser,12).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.form-control'))
        )
    input1.send_keys(str(y))

    browser.find_element(By.CSS_SELECTOR, "button.btn#solve").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла