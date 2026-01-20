from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



try:
    link = 'https://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #ввод данных
    browser.find_element(By.NAME, 'firstname').send_keys('Yasha')
    browser.find_element(By.NAME, 'lastname').send_keys('Sheshukov')
    browser.find_element(By.NAME, 'email').send_keys('Yasha@mail.com')
    #получить файл

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element(By.NAME, 'file')
    element.send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()