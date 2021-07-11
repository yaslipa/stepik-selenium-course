import unittest
from time import sleep
from selenium import webdriver


link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()


def get_text(link):
    browser.get(link)

    browser.find_element_by_css_selector(
        'input[required].first').send_keys('Name')
    browser.find_element_by_css_selector(
        'input[required].second').send_keys('Surname')
    browser.find_element_by_css_selector(
        'input[required].third').send_keys('email@mail.com')
    browser.find_element_by_css_selector('button.btn').click()
    sleep(1)

    return browser.find_element_by_tag_name('h1').text


class TestLink(unittest.TestCase):
    def test_link1(self):
        self.assertEqual('Congratulations! You have successfully registered!',
                         get_text(link1), 'Wrong text')

    def test_link2(self):
        self.assertEqual('Congratulations! You have successfully registered!',
                         get_text(link2), 'Wrong text')


if __name__ == '__main__':
    unittest.main()
    browser.quit()
