import requests


class YandexDisk:

    def __init__(self, token: str):
        self.token = token

    def create_new_folder(self, folder_name: str) -> int:
        """
        Функция создает папку на ЯндексДиске
        :param folder_name: название новой папки
        :return: код ответа от YandexRESTAPI
        """

        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {"path": folder_name}
        response = requests.put(URL, headers=headers, params=params)
        return response.status_code
