import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URLS = (236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905)


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', URLS)
class TestAlienMessages:
    def test_find_hidden_text(self, browser, url):
        link = f'https://stepik.org/lesson/{url}/step/1'
        answer = math.log(int(time.time()))

        browser.get(link)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'textarea.string-quiz__textarea'))).send_keys(str(answer))
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'button.submit-submission'))).click()

        feedback = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.smart-hints__feedback'))).text
        assert feedback == 'Correct!', f'Текст фидбека не совпадает: {feedback}'
