import unittest
from katas.reduce_list import reduce_array


class TestReduceList(unittest.TestCase):
    def test_reduce_list(self):
        original_numbers = [10, 15, 7, 20, 25]
        reduce_array(original_numbers)
        self.assertEqual(original_numbers, [10,5,-8,13,5])
    def test_empty_reduce_list(self):
        original_numbers = []
        reduce_array(original_numbers)
        self.assertEqual(original_numbers, [])
    def test_equal_reduce_list(self):
        original_numbers = [5,5,5,5]
        reduce_array(original_numbers)
        self.assertEqual(original_numbers, [5,0,0,0])



