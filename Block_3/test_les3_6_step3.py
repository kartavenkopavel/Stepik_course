import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


@pytest.fixture()
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nbrowser quit")
    browser.quit()


class TestMain():
    links_array = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

    @pytest.mark.parametrize('links', links_array)
    def test_pages(self, browser, links):
        answer = math.log(int(time.time()))
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(answer))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button.click()
        time.sleep(2)
        message = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        print(f"\n{message}")
        assert message == "Correct!"

