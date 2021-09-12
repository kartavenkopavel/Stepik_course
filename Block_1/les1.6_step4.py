from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_field = browser.find_element_by_tag_name('input')
    first_name_field.send_keys('Ivan')
    last_name_field = browser.find_element_by_name('last_name')
    last_name_field.send_keys('Ivanov')
    city_field = browser.find_element_by_class_name('city')
    city_field.send_keys('Moscow')
    country_field =browser.find_element_by_id('country')
    country_field.send_keys('Russia')
    button = browser.find_elements_by_css_selector("button.bth")
    button.click()    

finally:
    time.sleep(10)
    browser.quit()

