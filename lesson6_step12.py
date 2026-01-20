from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link1 = "https://suninjuly.github.io/registration1.html"
    link2 = "https://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link2)  # тестируем первую страницу

    # УНИКАЛЬНЫЕ СЕЛЕКТОРЫ ДЛЯ СТРАНИЦЫ 1
    # На странице 2 этих элементов нет - будет ошибка

    # Поле "Input your first name" - на странице 2 placeholder другой!
    browser.find_element(By.CSS_SELECTOR, "input.first[placeholder*='name']").send_keys("Yasha")

    # Поле "Input your last name" - на странице 2 этого поля вообще нет!
    browser.find_element(By.CSS_SELECTOR, "input[placeholder*='last name']").send_keys("Sheshukov")

    # Поле email - селектор уникальный только для страницы 1
    browser.find_element(By.CSS_SELECTOR, "input.third[placeholder*='email']").send_keys("test@yasha.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()