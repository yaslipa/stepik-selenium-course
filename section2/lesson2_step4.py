from selenium import webdriver
from time import sleep


browser = webdriver.Chrome()

try:
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
    sleep(7)
    browser.quit()
