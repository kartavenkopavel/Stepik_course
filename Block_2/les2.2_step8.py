from selenium import webdriver
import os #импорт модуля для работы с файлами
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    #заполняем поля
    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys('Ivan')
    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys('Ivanov')
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys('example@example.com')
    #загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')        # добавляем к этому пути имя файла
    file = browser.find_element_by_css_selector("[type='file']")
    file.send_keys(file_path)
    #нажать на кнопку
    button = browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()