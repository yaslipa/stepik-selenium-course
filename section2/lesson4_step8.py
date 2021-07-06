import math
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()


def calc(num):
    return str(math.log(abs(12*math.sin(int(num)))))


# try:
browser.get(link)

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
browser.find_element(By.ID, 'book').click()

x = browser.find_element(By.ID, 'input_value').text
y = calc(x)
browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.ID, 'solve').click()
#
# finally:
#     # sleep(10)
#     browser.quit()
