from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    z = int(x) + int(y)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(z))

    browser.find_element_by_tag_name('button').click()

finally:
    sleep(10)
    browser.quit()
