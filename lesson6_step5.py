from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = ' http://suninjuly.github.io/find_link_text'

try:
    #открываем страницу в браузере
    browser = webdriver.Chrome()
    browser.get(link)

    #из условия находим название ссылки на которуую нужно нажать
    answer = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #print(answer)
    #ищем ссылку с таким текстом
    link_text = browser.find_element(By.LINK_TEXT, answer).click()

    #заполняем форму
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)

    browser.quit()

