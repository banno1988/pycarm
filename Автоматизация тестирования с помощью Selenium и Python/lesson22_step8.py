from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import os


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR,'input[name=firstname]').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR,'input[name=lastname]').send_keys("Grinin")
    browser.find_element(By.CSS_SELECTOR, 'input[name=email]').send_keys("1213@dfg.ru")
    #current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    #file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_path = "D:\\pycarm\\text.txt"
    print(file_path)
    element= browser.find_element(By.CSS_SELECTOR,'input[type="file"]')
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла