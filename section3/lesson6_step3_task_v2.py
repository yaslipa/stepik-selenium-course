import math
import time

import pytest
from selenium import webdriver

URLS = (236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905)
alien_message = ''


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(alien_message)


@pytest.fixture()
def answer():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('url', URLS)
def test_find_hidden_text(browser, url, answer):
    global alien_message
    link = f'https://stepik.org/lesson/{url}/step/1'
    browser.get(link)

    browser.find_element_by_class_name(
        'string-quiz__textarea').send_keys(answer)
    browser.find_element_by_css_selector(
        'button.submit-submission').click()
    feedback = browser.find_element_by_class_name(
        'smart-hints__feedback').text

    try:
        assert feedback == 'Correct!', f'Текст фидбека не совпадает: {feedback}'
    except AssertionError:
        alien_message += feedback
