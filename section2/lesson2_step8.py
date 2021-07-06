import os
from time import sleep
from selenium import webdriver


link = 'http://suninjuly.github.io/file_input.html'
# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'blank.txt')

browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('Имя')
    browser.find_element_by_name('lastname').send_keys('Фамилия')
    browser.find_element_by_name('email').send_keys('email@mail.com')

    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_tag_name('button').click()
finally:
    sleep(10)
    browser.quit()
