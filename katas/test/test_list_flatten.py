import unittest
from katas.list_flatten import flatten_list


class TestListFlatten(unittest.TestCase):
    def test_flatten(self):
        nested_list = [
            1,
            [2, 3],
            [4, [5, 6]],
            7
        ]
        flat_list = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_list(nested_list), flat_list)  # add assertion here

    def test_flatten_empty_list(self):
        nested = []
        self.assertEqual(flatten_list(nested), [])

    def test_flatten_single_element_nested(self):
        nested = [[[[2]]]]
        self.assertEqual(flatten_list(nested), [2])

    def test_flatten_mixed_empty_and_numbers(self):
        nested = [[[], []], [1, 2], [], 3]
        self.assertEqual(flatten_list(nested), [1, 2, 3])