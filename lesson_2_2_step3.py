from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #Сберем велью(текст) и считаем сумму
    x_element = int(browser.find_element(By.ID, 'num1').text)
    y_element = int(browser.find_element(By.ID, 'num2').text)
    summ = x_element + y_element
    # Открываем дропдаун и выбираем ответ
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summ))
    # нажимаем на сабмит
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()