import unittest
from katas.stock_trader_v2 import max_profit  # Adjust import path as needed

class TestMaxProfitMultiple(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 7)
        # Buy at 1, sell at 5 → profit = 4
        # Buy at 3, sell at 6 → profit = 3
        # Total = 7

    def test_increasing_prices(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)
        # Buy at 1, sell at 5 → or multiple buys/sells

    def test_decreasing_prices(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        # No profit possible

    def test_flat_prices(self):
        self.assertEqual(max_profit([3, 3, 3, 3]), 0)

    def test_single_day(self):
        self.assertEqual(max_profit([5]), 0)

    def test_two_days_profit(self):
        self.assertEqual(max_profit([1, 5]), 4)

    def test_two_days_loss(self):
        self.assertEqual(max_profit([5, 1]), 0)

    def test_alternate_up_down(self):
        self.assertEqual(max_profit([1, 3, 2, 4, 3, 5]), 6)
        # Profit = (3-1) + (4-2) + (5-3)

    def test_zero_prices(self):
        self.assertEqual(max_profit([0, 0, 0, 0]), 0)

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

if __name__ == '__main__':
    unittest.main()
