from bs4 import BeautifulSoup
import requests
from fake_headers import Headers
import json

URL = 'https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&excluded_text=&area=1&area=2&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50'

KEYWORDS = {'Django', 'Flask'}


def get_headers():
    '''
    Функция генерирует заголовки для скраппинга сайта
    :return: dict
    '''
    return Headers(browser='opera', os='win').generate()


def flat_generator(list_of_lists: list) -> list:
    '''
    Функция-генератор, распаковывает список списков.
    :param list_of_lists:
    :return:
    '''
    for lst in list_of_lists:
        yield from lst


def cook_soup(url: str, headers: dict, parser: str = 'html.parser') -> BeautifulSoup:
    '''
    Функция преобразует web-станицу по указанному адресу в объект bs4.BeautifulSoup для последующего парсинга
    :param url: строка с web-адресом страницы для парсинга
    :param headers: словарь с указанием необходимых параметров для осуществления get запроса
    :param parser: строка с указанием тип парсера из библиотеки bs4: 'html.parser', 'xml', 'lxml'*, 'html5lib'* (* - требуют отдельной установки)
    :return: BeautifulSoup.object
    '''
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, features=parser)
    return soup


def find_keywords(soup: BeautifulSoup, keywords: set) -> list:
    '''
    Функция осуществляет поиск по ключевым словам в тексте превью-вакансии (на странице с основными фильтрами)
    и в тексте вакансии (внутри отдельной страницы ванаксии)
    :param soup: объект BeautifulSoup
    :param keywords: объект множество с ключевыми словами
    :return: список совпадений - список словарей с результатми парсинга
    '''

    main_content = soup.find(id='a11y-main-content')
    vacancies = main_content.find_all('div', class_='serp-item')

    result = []
    counter = 0

    for vacancy in vacancies:

        vacancy_title = vacancy.find('a', class_='serp-item__title').text

        vacancy_preview = vacancy.find('div', class_='g-user-content')
        vacancy_preview_set = set(flat_generator([*[item.text.strip().split() for item in vacancy_preview]]))
        vacancy_preview = vacancy_preview.text

        link = vacancy.find('h3').find('a')['href']

        try:
            salary = vacancy.find('span', class_='bloko-header-section-3').text.replace(u'\u202f', ' ')
        except AttributeError:
            salary = 'Данные о заработной плате не указаны'

        company_name = vacancy.find(class_='bloko-link bloko-link_kind-tertiary').text.replace(u'\xa0', u' ')
        city = vacancy.find('div', class_= 'bloko-text').find_next(class_= 'bloko-text').text

        full_vacancy = cook_soup(link, headers=get_headers())
        try:
            full_vacancy_content = full_vacancy.find('div', class_='vacancy-description').find_all('p')
        except AttributeError:
            full_vacancy_content = full_vacancy.find('div', class_='vacancy-description').find_all('li')
        full_vacancy_content = set(flat_generator([*[item.text.strip().split() for item in full_vacancy_content]]))

        if (vacancy_preview_set & keywords) or (full_vacancy_content & keywords):
            result.append({
                'vacancy_title' : vacancy_title,
                'vacancy_preview' : vacancy_preview,
                'salary' : salary,
                'company_name' : company_name,
                'city' : city,
                'link' : link
            })
            counter += 1

    print(f'{"*" * 15} {counter} совпадений найдено {"*" * 15}')

    return result


def write_JSON(result: list, file_name: str) -> str:
    '''
    Функция для записи результатов парсинга в json-объект
    :param result: список словарей с результатами парсинга
    :param file_name: строка с именем файла
    :return: строка с описанием результата работы функции
    '''
    if result is []:
        return print('Данные для записи в json-файл отсутствуют')
    else:
        with open (file_name, 'w') as file:
            json.dump(result, file, indent=2, ensure_ascii=False)
    return print(f'Данные записаны в {file_name}')


def main(url: str, keywords: set):
    '''
    :param url: строка с web-адресом страницы для парсинга
    :param keywords: объект множество с ключевыми словами
    :return:
    '''
    soup = cook_soup(url, headers=get_headers())
    result = find_keywords(soup, keywords)
    write_JSON(result, file_name='result.json')


if __name__ == '__main__':

    main(url=URL, keywords=KEYWORDS)

