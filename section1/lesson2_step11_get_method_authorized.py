import time
from selenium import webdriver

# инициализируем драйвер браузера, открывается пустое окно браузера
driver = webdriver.Chrome()
time.sleep(5)

# открывается заданный урл
driver.get("https://stepik.org/lesson/25969/step/12?auth=login&unit=196192")
time.sleep(5)

# Проходим авторизацию
login = driver.find_element_by_css_selector("#id_login_email")
password = driver.find_element_by_css_selector("#id_login_password")
authorization_button = driver.find_element_by_css_selector(".sign-form__btn")

login.send_keys("slipa.box@gmail.com")
password.send_keys("steslipapik1977")
authorization_button.click()
time.sleep(5)

# Отвечаем на вопрос урока 12
try:
    textarea = driver.find_element_by_css_selector(".textarea")
    textarea.send_keys("get()")
    submit_button = driver.find_element_by_css_selector(".submit-submission")
    submit_button.click()
except Exception as e:
    again_button = driver.find_element_by_css_selector(".again-btn")
    again_button.click()
    time.sleep(5)
    textarea = driver.find_element_by_css_selector(".textarea")
    textarea.send_keys("get()")
    submit_button = driver.find_element_by_css_selector(".submit-submission")
    submit_button.click()

time.sleep(5)

# Закрываем окно браузера
driver.quit()
