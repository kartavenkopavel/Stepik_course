from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #находим скрытую ссылку по формуле str(math.ceil(math.pow(math.pi, math.e)*10000))
    hide_link = browser.find_element_by_link_text('224592').click()
    #заполняем форму
    first_name_field = browser.find_element_by_tag_name('input')
    first_name_field.send_keys('Ivan')
    last_name_field = browser.find_element_by_name('last_name')
    last_name_field.send_keys('Ivanov')
    city_field = browser.find_element_by_class_name('city')
    city_field.send_keys('Moscow')
    country_field =browser.find_element_by_id('country')
    country_field.send_keys('Russia')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
