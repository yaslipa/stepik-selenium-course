from selenium import webdriver
from time import sleep

link = 'http://suninjuly.github.io/registration1.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Заполняем обязательные поля
    input1 = browser.find_element_by_css_selector('input[required].first')
    input1.send_keys('Name')
    input2 = browser.find_element_by_css_selector('input[required].second')
    input2.send_keys('Surname')
    input3 = browser.find_element_by_css_selector('input[required].third')
    input3.send_keys('email@mail.com')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    sleep(10)
    browser.quit()
