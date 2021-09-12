from selenium import webdriver
import time
import math

def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()#развернуть окно
    #найти значение х
    find_x = browser.find_element_by_id("input_value").text
    answer = func(find_x)
    #ввод решения уравнения в поле
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(answer)
    #скролл вниз
    browser.execute_script("window.scrollBy(0, 100);")
    #нажать чекбокс 
    chekbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    #нажать радиоаттон робот
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']").click()    
    #нажать кнопку
    button = browser.find_element_by_tag_name("button").click()
    
finally:
    time.sleep(10)
    browser.quit()