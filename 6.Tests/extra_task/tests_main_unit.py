from unittest import TestCase, main
from unittest.mock import patch

from main import *


class TestCheckDocumentExistance(TestCase):

    def test_user_doc_number(self):
        self.assertEqual(check_document_existance('11-2'), True)
        self.assertNotEqual(check_document_existance('11-2'), False)
        self.assertEqual(check_document_existance('151'), False)
        self.assertNotEqual(check_document_existance('151'), True)


class TestGetDocOwnerName(TestCase):

    @patch('builtins.input')
    def test_input_1(self, input_mock):
        input_mock.return_value = '11-2'
        self.assertEqual(get_doc_owner_name(), "Геннадий Покемонов")
        self.assertNotEqual(get_doc_owner_name(), "Bill Gates")

    @patch('builtins.input')
    def test_input_2(self, input_mock):
        input_mock.return_value = '10006'
        self.assertEqual(get_doc_owner_name(), "Аристарх Павлов")
        self.assertNotEqual(get_doc_owner_name(), None)


class TestGetAllDocOwnersNames(TestCase):

    def test_user_list(self):
        self.assertEqual(get_all_doc_owners_names(), {'Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'})
        self.assertNotEqual(get_all_doc_owners_names(), ['Аристарх Павлов', 'Василий Гупкин', 'Геннадий Покемонов'])


class TestAddNewShelf(TestCase):

    def test_shelf_number(self):
        self.assertEqual(add_new_shelf('2'), ('2', False))
        self.assertNotEqual(add_new_shelf('2'), ('2', True))
        self.assertEqual(add_new_shelf('4'), ('4', True))
        self.assertNotEqual(add_new_shelf('4'), ('4', True))

    @patch('builtins.input')
    def test_shelf_number_input(self, input_mock):
        input_mock.return_value = '5'
        self.assertEqual(add_new_shelf(), ('5', True))
        self.assertNotEqual(add_new_shelf(), ('5', True))
        self.assertNotEqual(add_new_shelf('5'), ('5', True))


class TestDeleteDoc(TestCase):

    @patch('builtins.input')
    def test_delete_doc_input(self, input_mock):
        input_mock.return_value = '2207 876234'
        self.assertEqual(delete_doc(), ('2207 876234', True))


class TestGetDocShelf(TestCase):

    @patch('builtins.input')
    def test_get_shelf_input(self, input_mock):
        input_mock.return_value = '11-2'
        self.assertEqual(get_doc_shelf(), '1')
        self.assertNotEqual(get_doc_shelf(), None)


class TestAddNewDoc(TestCase):

    @patch('builtins.input')
    def test_add_new_doc_input(self, input_mock):
        input_mock.return_value = '7'
        self.assertNotEqual(add_new_doc(), None)
        self.assertEqual(add_new_doc(), '7')


if __name__ == '__main__':
    main()
