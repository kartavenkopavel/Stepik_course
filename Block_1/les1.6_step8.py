from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

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
    button = browser.find_element_by_xpath('//div[6]/button[3]')
    button.click()    

finally:
    time.sleep(10)
    browser.quit()

