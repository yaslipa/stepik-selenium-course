from selenium import webdriver
from time import sleep
import math


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    input_answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobtn = browser.find_element_by_id('robotsRule')
    radiobtn.click()
    submit_btn = browser.find_element_by_css_selector('button[type="submit"]')
    submit_btn.click()
finally:
    sleep(7)
    browser.quit()
