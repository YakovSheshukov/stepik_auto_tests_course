from operator import truediv

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    treasure_img = browser.find_element(By.ID, "treasure")
    print("✅ Сундук найден на странице!")
    x = treasure_img.get_attribute("valuex")
    y = calc(x)
    print(y)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()