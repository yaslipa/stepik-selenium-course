import math
from time import sleep
from selenium import webdriver


link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()


def calc(num):
    return str(math.log(abs(12*math.sin(int(num)))))


try:
    browser.get(link)

    browser.find_element_by_tag_name('button').click()
    browser.switch_to.alert.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_tag_name('button').click()
finally:
    sleep(10)
    browser.quit()
