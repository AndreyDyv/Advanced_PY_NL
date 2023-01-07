class FlatIterator:

    def __init__(self, list_of_lists):

        self.list_of_lists = list_of_lists
        self.max = len(list_of_lists)

    def __iter__(self):

        self.start = -1
        self.nested_list = iter([])
        return self

    def __next__(self):

        try:
            item = next(self.nested_list)
        except StopIteration:
            self.start += 1
            if self.start == self.max:
                raise StopIteration
            nested_list = self.list_of_lists[self.start]
            self.nested_list = iter(nested_list)
            item = next(self.nested_list)
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]
    flIt = FlatIterator(list_of_lists_1)
    print(list(flIt))
