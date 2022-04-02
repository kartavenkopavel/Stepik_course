from selenium import webdriver
import time

# url страницы
link = "http://suninjuly.github.io/math.html"

# открываем страницу
browser = webdriver.Chrome()
browser.get(link)
# проверка, что радиобаттон по-умолчанию на "people rule"
people_radio = browser.find_element_by_id('peopleRule')
people_checked = people_radio.get_attribute('checked')
print('value of people radio: ', people_checked)
assert people_checked is not None, "People radio in not select by default"

# проверка, что радиобаттон "robot rule" не по-умолчанию
robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

browser.quit()
