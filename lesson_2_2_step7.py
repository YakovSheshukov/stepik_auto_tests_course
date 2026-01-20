from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #Сберем велью(текст) и считаем сумму
    x_element = browser.find_element(By.ID,'input_value').text
    y = calc(x_element)
    browser.find_element(By.ID,'answer').send_keys(y)
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()