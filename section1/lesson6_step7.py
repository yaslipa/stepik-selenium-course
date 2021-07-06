from time import sleep
from selenium import webdriver


url = 'http://suninjuly.github.io/huge_form.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys('Заполнено')
    btn = browser.find_element_by_css_selector('button.btn')
    btn.click()
finally:
    sleep(30)
    browser.quit()
