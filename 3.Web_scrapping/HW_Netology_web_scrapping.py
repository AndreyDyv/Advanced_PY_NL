from bs4 import BeautifulSoup
import requests
import time

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Python', 'БД', 'PostgreSQL', 'Читальный зал']

URL = 'https://habr.com/ru/all/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


def cooking_soup(url: str, headers: dict, parser_type: str = 'html.parser') -> BeautifulSoup:
    '''
    Функция преобразует web-станицу по указанному адресу в объект bs4.BeautifulSoup для последующего парсинга
    :param url: строка с web-адресом страницы для парсинга
    :param headers: словарь с указанием необходимых параметров для осуществления get запроса
    :param parser: строка с указанием тип парсера из библиотеки bs4: 'html.parser', 'xml', 'lxml'*, 'html5lib'* (* - требуют отдельной установки)
    :return: BeautifulSoup.object
    '''
    response = requests.get(url, headers=headers)
    time.sleep(0.3)
    text = response.text
    soup = BeautifulSoup(text, features=parser_type)
    return soup


def flat_generator(list_of_lists: list) -> list:
    '''
    Функция-генератор, распаковывает список списков.
    :param list_of_lists:
    :return:
    '''
    for lst in list_of_lists:
        yield from lst


def find_keywords(soup: BeautifulSoup, KEYWORDS: list):
    '''
    Функция находит совпадения из списка ключевых слов и информации из хабов, названия и превью статей,
    и выводит совпадения в формате <дата> - <заголовок> - <ссылка>
    :param soup: BeautifulSoup.object
    :param KEYWORDS: список ключевых слов для поиска статей
    :return: None
    '''

    articles = soup.find(class_='tm-articles-list').find_all('article')

    for article in articles:

        hubs = article.find_all(class_='tm-article-snippet__hubs-item')
        hubs = {word.find('a').text.strip() for word in hubs}

        preview = article.find(class_='article-formatted-body').find_all('p')
        # print(preview)
        # preview = [i.split() for i in [*[item.text for item in preview]]]
        preview = [*[item.text.split() for item in preview]]
        preview = list(flat_generator(preview))
        # print(preview)
        # print(type(preview))

        date = article.find('time').get('title')

        title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text

        href = f"https://habr.com{article.find('a', class_='tm-article-snippet__title-link').get('href')}"

        if hubs & set(KEYWORDS):
            print(f'Совпадение по хабам {date} --> {title} --> {href}')
            print('*************')

        for keyword in KEYWORDS:
            title2 = title.split()
            if keyword in title2:
                print(f'Совпадение в названии статьи {date} --> {title} --> {href}')
                print('*************')
            if keyword in preview:
                print(f'Совпадение в превью статьи {date} --> {title} --> {href}')
                print('*************')


        # print(article)
        # print()
        # print('*****************************************')
        # print()


if __name__ == '__main__':

    soup = cooking_soup(url=URL, headers=HEADERS)
    find_keywords(soup, KEYWORDS)

