import unittest
from katas.true_counter import count_true_values


class TestTrueCounter(unittest.TestCase):
    def test_true_counter(self):
        self.assertEqual(count_true_values([True,True,False]), 2)

    def test_all_false_true_counter(self):
        self.assertEqual(count_true_values([False, False, False,False,False]), 0)

    def test_empty_true_counter(self):
        self.assertEqual(count_true_values([]), 0)




