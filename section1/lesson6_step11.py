from selenium import webdriver
from time import sleep

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()

try:
    # Тест успешно проходит на странице link1
    browser.get(link1)

    # Тест падает на странице link2 с ошибкой NoSuchElementException
    browser.get(link2)

    input1 = browser.find_element_by_css_selector('input[required].first')
    input1.send_keys('Name')
    input2 = browser.find_element_by_css_selector('input[required].second')
    input2.send_keys('Surname')
    input3 = browser.find_element_by_css_selector('input[required].third')
    input3.send_keys('email@mail.com')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    sleep(10)
    browser.quit()
