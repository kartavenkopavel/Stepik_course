from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)
    button = browser.find_element(By.ID, "submit_button").click()

    time.sleep(2)

except Exception:
    print('Error')

    
finally:
    browser.quit()
    print('You find button!')
