class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index_1 = 0
        self.index_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index_1 < len(self.list_of_list) and self.index_2 == len(self.list_of_list[self.index_1]):
            self.index_1 += 1
            self.index_2 = 0

        if self.index_1 >= len(self.list_of_list):
            raise StopIteration

        item = self.list_of_list[self.index_1][self.index_2]
        self.index_2 += 1

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
        print(flat_iterator_item, check_item)
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

import types

'''Номер 2'''


def flat_generator(list_of_lists):
    index_1 = 0
    index_2 = 0

    while index_1 < len(list_of_lists):
        try:
            item = list_of_lists[index_1][index_2]
            index_2 += 1
            yield item
        except IndexError:
            index_2 *= 0
            index_1 += 1


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()








#первый код
# class FlatIterator:
#
#     def __init__(self, list_of_list):
#         self.list_of_list = list_of_list
#
#     def __iter__(self):
#         self.index_1 = 0
#         self.index_2 = 0
#
#         return self
#
#     def __next__(self):
#         try:
#             item = self.list_of_list[self.index_1][self.index_2]
#             self.index_2 += 1
#             return item
#
#         except IndexError:
#             self.index_2 = 0
#             self.index_1 += 1
#
#         if self.index_1 > len(self.list_of_list) - 1:
#             raise StopIteration
#
# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
# bla = FlatIterator(list_of_lists_1)
# for item in bla:
#     print(item)