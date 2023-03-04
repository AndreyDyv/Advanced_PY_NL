from time import sleep

from selenium.webdriver import Chrome

login = ''
password = ''
browser = Chrome('chromedriver')
URL = 'https://passport.yandex.ru/auth/'


def ya_author_selenium(URL, login, password):
    browser.get(URL)

    login_fill = browser.find_element('name', 'login')
    login_fill.send_keys(login)
    browser.find_element('id', "passp:sign-in").click()

    sleep(5)

    password_fill = browser.find_element('name', 'passwd')
    password_fill.send_keys(password)
    browser.find_element('id', "passp:sign-in").click()

    sleep(5)

    return browser.title
