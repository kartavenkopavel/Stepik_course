import unittest
from selenium import webdriver
import time


class TestSuits(unittest.TestCase):

    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        #заполнить только обязательные поля
        first_name_field = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input')
        first_name_field.send_keys('Ivan')
        last_name_field = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input')
        last_name_field.send_keys('Ivanov')
        email_field = browser.find_element_by_class_name('third')
        email_field.send_keys('exaple@example.com')
        #отправить форму
        button = browser.find_element_by_css_selector("body > div > form > button").click()
        time.sleep(2)

        #найти элемент с текстом
        text_element = browser.find_element_by_tag_name('h1')
        #записать текст в переменную для сравнения
        text = text_element.text

        #сравнение текста
        self.assertEqual("Congratulations! You have successfully registered!", text)
    
    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)
        #заполнить только обязательные поля
        first_name_field = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.first_class > input')
        first_name_field.send_keys('Ivan')
        last_name_field = browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input')
        last_name_field.send_keys('Ivanov')
        email_field = browser.find_element_by_class_name('third')
        email_field.send_keys('exaple@example.com')
        #отправить форму
        button = browser.find_element_by_css_selector("body > div > form > button").click()
        time.sleep(2)

        #найти элемент с текстом
        text_element = browser.find_element_by_tag_name('h1')
        #записать текст в переменную для сравнения
        text = text_element.text

        #сравнение текста
        self.assertEqual("Congratulations! You have successfully registered!", text)

if __name__ == "__main__":
    unittest.main()