from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все поля формы
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    # или elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполняем каждое поле
    for element in elements:
        element.send_keys("Мой ответ")

    # Находим и нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# Пустая строка в конце файла