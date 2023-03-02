import pytest

from Netology_HW_unittest_pytest.Netology_HW_unittest_pytest_task_no_number.fixtures_main_pytest import *
from main import *


@pytest.mark.parametrize('doc_num, result', fixture_check_doc_exist)
def test_check_document_existance(doc_num, result):
    assert check_document_existance(doc_num) == result


def test_get_doc_owner_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10006')
    assert get_doc_owner_name() == 'Аристарх Павлов'


def test_get_all_doc_owners_names():
    assert get_all_doc_owners_names() == {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}


@pytest.mark.parametrize('doc_num, result', fixture_remove_doc)
def test_remove_doc_from_shelf(doc_num, result):
    assert remove_doc_from_shelf(doc_num) == result


@pytest.mark.parametrize('shelf, result', fixture_shelf_number)
def test_add_new_shelf(shelf, result):
    assert add_new_shelf(shelf) == result


@pytest.mark.parametrize('doc_num, shelf, result', fixture_append_doc_to_shelf)
def test_append_doc_to_shelf(doc_num, shelf, result):
    assert append_doc_to_shelf(doc_num, shelf) == result


def test_delete_doc(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10006')
    assert delete_doc() == ('10006', True)


def test_get_doc_shelf(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '11-2')
    assert get_doc_shelf() == '1'


def test_move_doc_to_shelf(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: ('5455 028765', '3'))
    assert move_doc_to_shelf() == None


@pytest.mark.parametrize('doc_num, result', fixture_doc_info)
def test_show_document_info(doc_num, result):
    assert show_document_info(doc_num) == result


def test_show_all_docs_info():
    assert show_all_docs_info() == None
    assert show_all_docs_info() != True


def test_add_new_doc(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '6')
    assert add_new_doc() == '6'


if __name__ == '__main__':
    test_check_document_existance()
    test_get_doc_owner_name()
    test_get_all_doc_owners_names()
    test_remove_doc_from_shelf()
    test_add_new_shelf()
    test_append_doc_to_shelf()
    test_delete_doc()
    test_get_doc_shelf()
    test_move_doc_to_shelf()
    test_show_document_info()
    test_show_all_docs_info()
    test_add_new_doc()
