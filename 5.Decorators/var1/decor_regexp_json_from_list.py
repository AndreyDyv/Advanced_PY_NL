import csv
import re

from tools_json_from_list import logger_decor_param

phone_search_pattern = r"(\+7|8)[\s(-]*(\d{3})[-)\s]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(доб\.)*\s*(\d{4})*[\)]*"
phone_replace_pattern = r"+7(\2)\3-\4-\5 \6 \7"


@logger_decor_param(log_path='log_book_list.json')
def open_csv_file(file: str) -> list:
    '''
    Функция получает содержимое переданного csv-файла.
    :param file: имя обрабатываемого файла.
    :return: содержимое файла в виде списка списков
    '''
    with open(file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


@logger_decor_param(log_path='log_book_list.json')
def write_phonebook(phonebook: list) -> None:
    '''
    Функция записывает отформатированные контакты в итоговый файл.
    :param phonebook: отформатированный список контактов для записи в файл.
    :return: None
    '''
    with open("phonebook.csv", "w", encoding='UTF-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(phonebook)


@logger_decor_param(log_path='log_book_list.json')
def standardize_csv_file(contacts_list: list) -> list:
    '''
    Функция преобразует все данные во вложенных списках к стандартному шаблону
    [lastname, firstname, surname, organization, position, phone, email]
    Позиция phone обрабатывается как regular expression.
    Шаблон для обработки phone вынесен за пределы функции
    в переменные phone_search_pattern и phone_replace_pattern
    :param contacts_list: список списков, полученный из файла
    :return: отформатированный по шаблону список списков
    '''
    standardized_contacts_list = []
    for index, value in enumerate(contacts_list):
        name_string = ' '.join(value[0:3])
        name_list = name_string.split()
        if len(name_list) == 3:
            lastname = name_list[0]
            firstname = name_list[1]
            surname = name_list[2]
        if len(name_list) == 2:
            lastname = name_list[0]
            firstname = name_list[1]
            surname = ''
        organization = value[3]
        position = value[-3]
        phone = re.sub(phone_search_pattern, phone_replace_pattern, value[-2]).strip()
        email = value[-1].strip()
        standardized_contacts_list.append([lastname, firstname, surname, organization, position, phone, email])
    return standardized_contacts_list


@logger_decor_param(log_path='log_book_list.json')
def get_phonebook(standardized_contacts_list: list) -> list:
    '''
    Функция проверяет отформатированный по шаблону список контактов на наличие дублирующихся контактов,
    объединяет данные в дублирующихся контактах, удаляет дублирующиеся контакты
    и добавляет в список новые контакты, полученные из объединенных данных.
    :param standardized_contacts_list: отформатированный по шаблону список списков.
    :return: список для записи в файл
    '''
    unique_contacts_dict = {}
    unique_contacts_list = []
    joint_contacts_list = []
    remove_positions_list = []

    for index, line in enumerate(standardized_contacts_list):
        if line[0] in unique_contacts_dict:
            joint_contact = [i or j for i, j in zip(line, standardized_contacts_list[unique_contacts_dict[line[0]]])]
            joint_contacts_list.append(joint_contact)
        else:
            unique_contacts_dict[line[0]] = index
            unique_contacts_list.append(line)

    for index, line in enumerate(unique_contacts_list):
        for i, row in enumerate(joint_contacts_list):
            if line[0] == row[0]:
                remove_positions_list.append(line)

    unique_contacts_list.extend(joint_contacts_list)

    for line in unique_contacts_list:
        if line in remove_positions_list:
            unique_contacts_list.remove(line)

    return unique_contacts_list


@logger_decor_param(log_path='log_book_list.json')
def main(csv_file: str) -> None:
    '''
    Функция запускает программу обработки и записи телефонной книги.
    :param csv_file: имя обрабатываемого файла.
    :return: None
    '''
    contacts_list = open_csv_file(csv_file)
    standardized_list = standardize_csv_file(contacts_list)
    phonebook = get_phonebook(standardized_list)
    write_phonebook(phonebook)


if __name__ == '__main__':
    main('phonebook_raw.csv')
