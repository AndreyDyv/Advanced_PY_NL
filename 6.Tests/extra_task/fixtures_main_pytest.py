fixture_check_doc_exist = [
    ('11-2', True),
    ('1100', False),
    ('', False),
    ('2207 876234', True)
]

fixture_remove_doc = [
    ('1100', None),
    ('', None),
]

fixture_shelf_number = [
    ('2', ('2', False)),
    ('4', ('4', True)),
    ('1', ('1', False))
]

fixture_append_doc_to_shelf = [
    ('1', '123', None),
    ('3', '777', None),
    ('7', 'number', None)
]

fixture_doc_info = [
    ({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, None),
    ({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}, None),
    ({"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}, None)
]
