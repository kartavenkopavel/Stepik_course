from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
#функция для вычисления суммы чисел
def sum(x, y):
    return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #находим значения двух чисел
    find_x = browser.find_element_by_id("num1").text
    find_y = browser.find_element_by_id("num2").text
    #вызываем функцию sum
    answer = sum(find_x, find_y)
    #выбираем и списка правильный ответ
    inpit_field = Select(browser.find_element_by_tag_name("select"))
    inpit_field.select_by_value(answer) 
    button = browser.find_element_by_tag_name("button").click()
    
finally:
    time.sleep(10)
    browser.quit()
