from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #найти значение х
    img_elem = browser.find_element_by_id("treasure")
    x_value = img_elem.get_attribute("valuex")
    x = x_value
    func_x = calc(x)
    #ввод значения в поле
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(func_x)
    #нажать чекбокс
    chekbox = browser.find_element_by_id("robotCheckbox").click()
    #нажать правильный радиобаттон
    radiobutton = browser.find_element_by_id("robotsRule").click()
    #нажать на кнопку
    button = browser.find_element_by_css_selector("div > button").click()

finally:
    time.sleep(10)
    browser.quit()
    