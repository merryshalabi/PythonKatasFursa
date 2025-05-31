import unittest
from katas.stock_trader import max_profit  # Adjust import path if needed

class TestMaxProfit(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_decreasing_prices(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_increasing_prices(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

    def test_single_element(self):
        self.assertEqual(max_profit([5]), 0)

    def test_two_elements_profit(self):
        self.assertEqual(max_profit([1, 10]), 9)

    def test_two_elements_loss(self):
        self.assertEqual(max_profit([10, 1]), 0)

    def test_flat_prices(self):
        self.assertEqual(max_profit([3, 3, 3, 3]), 0)

    def test_profit_just_before_last(self):
        self.assertEqual(max_profit([9, 2, 6, 1, 8, 3]), 7)  # buy at 1, sell at 8

    def test_profit_with_early_drop(self):
        self.assertEqual(max_profit([5, 1, 4, 2, 6]), 5)  # buy at 1, sell at 6

if __name__ == '__main__':
    unittest.main()
