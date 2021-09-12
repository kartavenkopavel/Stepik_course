from selenium import webdriver
from formula import calc

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button").click()
    #переход на новую вкладку
    name_window = browser.window_handles[1] #показывает новую вкладку
    new_browser_tab = browser.switch_to.window(name_window)    
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
