def geo_logs_filter(geo_logs_list: list) -> list:
    '''
    Функция фильтрует список визитов по указанному пользователем запросу: стране визита
    :param geo_logs_list: список визитов следующего вида: list[dict[str, list[str]] | dict[str, list[str]] ... ]
    :return: отфильтрованный список с результатами запроса
    '''

    filter_ = input('Введите название страны: ')
    result = []
    for visit in geo_logs_list:
        if filter_ in list(visit.values())[0]:
            result.append(visit)
    if result == []:
        return 'Поиск по указанному вами фильтру не дал результатов'

    return result


def get_values_from_ids(ids: dict) -> list:
    '''
    Функция возвращает список уникальных числовых значений (int) в словаре ids
    :param ids: словарь следующего вида  dict[str: list[int]]
    :return: список уникальных числовых значений
    '''

    result = set()
    for item in ids.values():
        result.update(item)

    return list(result)


def queries_analize(queries_list: list) -> list:
    '''
    Функция подсчитывает количество слов в поисковых запросах и отображает результат в процентах
    :param queries_list: список строк с поисковыми запросами
    :return: список строк с результатом анализа поисковых запросов
    '''

    result = []
    dict_q = {}
    for query in queries_list:
        words_counter = len(query.split(' '))
        if words_counter in dict_q:
            dict_q[words_counter] += 1
        else:
            dict_q[words_counter] = 1

    len_q = len(queries_list)

    for count_w, count_t in dict_q.items():
        result.append(f'Количество поисковых запросов из {count_w} слов - {count_t * 100 // len_q} %')

    return result
