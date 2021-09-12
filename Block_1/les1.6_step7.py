from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Answer")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
except Exception:
    print('Error')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()    
