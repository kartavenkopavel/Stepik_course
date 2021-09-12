from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from formula import calc

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    #ожидание пока цена не будет равна 100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) 
    book_button = browser.find_element_by_id("book").click()
    #скролл вниз до конца страницы
    browser.find_element_by_tag_name('body').send_keys(Keys.END)
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

