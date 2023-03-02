from unittest import TestCase, main
from unittest.mock import patch

from HW_task1 import geo_logs_filter, get_values_from_ids, queries_analize
from Netology_HW_unittest_pytest.Netology_HW_unittest_pytest_task1.fixtures_HW_task1 import *


class TestGeoLogsFilter(TestCase):

    @patch('builtins.input')
    def test_input(self, input_mock):
        input_mock.return_value = 'Россия'
        self.assertEqual(geo_logs_filter(geo_logs), rus_filter_output)
        self.assertNotEqual(geo_logs_filter(geo_logs), india_filter_output)
        self.assertNotEqual(geo_logs_filter(geo_logs), None)

        input_mock.return_value = 'Индия'
        self.assertEqual(geo_logs_filter(geo_logs), india_filter_output)
        self.assertNotEqual(geo_logs_filter(geo_logs), rus_filter_output)
        self.assertNotEqual(geo_logs_filter(geo_logs), None)

        input_mock.return_value = 'USA'
        self.assertEqual(geo_logs_filter(geo_logs), negative_output)
        self.assertNotEqual(geo_logs_filter(geo_logs), None)

    @patch('builtins.input')
    def test_args_instance(self, input_mock):
        input_mock.return_value = 'Россия'
        self.assertIsInstance(geo_logs_filter(geo_logs), list)
        self.assertNotIsInstance(geo_logs_filter(geo_logs), (dict, str, tuple, int, float, set, frozenset))
        self.assertIsInstance(geo_logs, list)
        self.assertNotIsInstance(geo_logs, (dict, str, tuple, int, float, set, frozenset))

    @patch('builtins.input')
    def test_args_errors(self, input_mock):
        input_mock.return_value = 'Россия'

        with self.assertRaises(AttributeError) as e:
            geo_logs_filter(geo_logs_dict)
        self.assertEqual("'str' object has no attribute 'values'", e.exception.args[0])

        with self.assertRaises(AttributeError) as e:
            geo_logs_filter('geo_log')
        self.assertEqual("'str' object has no attribute 'values'", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            geo_logs_filter(geo_logs, 'Россия')
        self.assertEqual('geo_logs_filter() takes 1 positional argument but 2 were given', e.exception.args[0])

        with self.assertRaises(AttributeError) as e:
            geo_logs_filter(geo_logs_broken)
        self.assertEqual("'list' object has no attribute 'values'", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            geo_logs_filter()
        self.assertEqual("geo_logs_filter() missing 1 required positional argument: 'geo_logs_list'",
                         e.exception.args[0])


class TestGetValuesFromIds(TestCase):

    def test_arg_output(self):
        self.assertEqual(get_values_from_ids(ids), ids_correct_output)
        self.assertNotEqual(get_values_from_ids(ids), ids_broken_output)
        self.assertNotEqual(get_values_from_ids(ids), None)
        self.assertNotEqual(get_values_from_ids(ids), '')
        self.assertNotEqual(get_values_from_ids(ids), {})

    def test_args_instance(self):
        self.assertIsInstance(get_values_from_ids(ids), list)
        self.assertNotIsInstance(get_values_from_ids(ids), (dict, str, tuple, int, float, set, frozenset))
        self.assertIsInstance(ids, dict)
        self.assertNotIsInstance(ids, (list, str, tuple, int, float, set, frozenset))

    def test_args_errors(self):
        with self.assertRaises(AttributeError) as e:
            get_values_from_ids(ids_list)
        self.assertEqual("'list' object has no attribute 'values'", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            get_values_from_ids()
        self.assertEqual("get_values_from_ids() missing 1 required positional argument: 'ids'", e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            get_values_from_ids(ids, None)
        self.assertEqual('get_values_from_ids() takes 1 positional argument but 2 were given', e.exception.args[0])


class TestQueriesAnalize(TestCase):

    def test_arg_output(self):
        self.assertEqual(queries_analize(queries), queries_correct_output)
        self.assertNotEquals(queries_analize(queries), None, [])
        self.assertNotEquals(queries_analize(queries), '', {})

    def test_args_instance(self):
        self.assertIsInstance(queries_analize(queries), list)
        self.assertNotIsInstance(queries_analize(queries), (dict, str, tuple, int, float, set, frozenset))
        self.assertIsInstance(queries, list)
        self.assertNotIsInstance(queries, (dict, str, tuple, int, float, set, frozenset))

    def test_args_errors(self):
        with self.assertRaises(TypeError) as e:
            queries_analize()
        self.assertEqual("queries_analize() missing 1 required positional argument: 'queries_list'",
                         e.exception.args[0])

        with self.assertRaises(TypeError) as e:
            queries_analize(queries, None)
        self.assertEqual('queries_analize() takes 1 positional argument but 2 were given', e.exception.args[0])


if __name__ == '__main__':
    main()
