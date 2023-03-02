from unittest import TestCase, main

import requests

from yandex_api import YandexDisk


class TestYandexDisk(TestCase):

    def setUp(self):
        with open('pass.txt', encoding='UTF-8') as file_obj:
            token = file_obj.read()
        self.ya = YandexDisk(token)

        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.ya.token}'}
        params = {"path": 'Test_netology_folder', 'permanently': 'true'}
        requests.delete(URL, headers=headers, params=params)

    def test_creation_status_201(self):
        self.assertEqual(self.ya.create_new_folder('Test_netology_folder'), 201)

    def test_folder_on_disk_409(self):
        self.ya.create_new_folder('Test_netology_folder')
        self.assertEqual(self.ya.create_new_folder('Test_netology_folder'), 409)

    def test_broken_token_401(self):
        self.ya.token = 'broken_token'
        self.assertEqual(self.ya.create_new_folder('Test_netology_folder'), 401)
    
    def tearDown(self):
        URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.ya.token}'}
        params = {"path": 'Test_netology_folder', 'permanently': 'true'}
        requests.delete(URL, headers=headers, params=params)

if __name__ == '__main__':
    main()
