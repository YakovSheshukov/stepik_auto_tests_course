from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))




try:
    link = 'https://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, 'input_value').text
    y = calc(x_element)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    time.sleep(10)
    browser.quit()