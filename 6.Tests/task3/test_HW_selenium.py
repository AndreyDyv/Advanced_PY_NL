from HW_selenium import *


def test_selenium():
    assert ya_author_selenium(URL, login, password) == 'Авторизация'


if __name__ == '__main__':
    test_selenium()
