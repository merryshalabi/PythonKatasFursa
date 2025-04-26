
import unittest
from katas.list_diff import find_difference

class TestFindDifference(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)

    def test_all_same_values(self):
        self.assertEqual(find_difference([7, 7, 7]), 0)

    def test_two_elements(self):
        self.assertEqual(find_difference([5, 10]), 5)
        self.assertEqual(find_difference([10, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_difference([-10, -3, -20, -1]), 19)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(find_difference([-100, 0, 100]), 200)

    def test_single_element(self):
        self.assertEqual(find_difference([5]), 0)