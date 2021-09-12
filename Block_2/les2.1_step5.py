from selenium import webdriver
import math
import time

#фунция для вычисления 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#url страницы    
link = "http://suninjuly.github.io/math.html"

try:
    #открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)
    #нахождение значения х
    x_value = browser.find_element_by_id('input_value')
    x = x_value.text
    func_x = calc(x)
    #запись х в поле 
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(func_x)
    #нажать чекбокс
    chekbox = browser.find_element_by_css_selector("[for='robotCheckbox").click()
    #нажать правильный радиобаттон
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule").click()
    #нажать на кнопку
    button = browser.find_element_by_css_selector(" form > button").click()

except Exception:
    print("Error")    

finally:
    time.sleep(10)
    browser.quit()
