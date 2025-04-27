import unittest
from katas.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits(self):
        input_str = "abc333"
        self.assertEqual(sum_of_digits(input_str), 9)

    def test_empty_sum_of_digits(self):
        input_str = ""
        self.assertEqual(sum_of_digits(input_str), 0)

    def test_no_digits_sum_of_digits(self):
        input_str = "abc"
        self.assertEqual(sum_of_digits(input_str), 0)

