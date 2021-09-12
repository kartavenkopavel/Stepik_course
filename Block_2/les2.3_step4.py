from selenium import webdriver
from formula import calc

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button").click()
    #нажать на ок в всплывающем окне
    confirm = browser.switch_to.alert
    confirm.accept()
    #найти значение х
    find_x = browser.find_element_by_id("input_value").text
    answer = calc(find_x)
    #ввод решения уравнения в поле
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(answer)
    button = browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()
