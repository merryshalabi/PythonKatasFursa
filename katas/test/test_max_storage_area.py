import unittest
from katas.max_storage_capacity import max_storage_area  # adjust path if needed

class TestMaxStorageArea(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(max_storage_area([2, 1, 5, 6, 2, 3]), 10)

    def test_single_bar(self):
        self.assertEqual(max_storage_area([4]), 4)

    def test_ascending_bars(self):
        self.assertEqual(max_storage_area([1, 2, 3, 4, 5]), 9)  # height=3, width=3

    def test_descending_bars(self):
        self.assertEqual(max_storage_area([5, 4, 3, 2, 1]), 9)  # height=3, width=3

    def test_all_same_height(self):
        self.assertEqual(max_storage_area([2, 2, 2, 2]), 8)  # 2 * 4

    def test_with_zero_height(self):
        self.assertEqual(max_storage_area([0, 1, 0, 1]), 1)

    def test_empty(self):
        self.assertEqual(max_storage_area([]), 0)

    def test_two_bars(self):
        self.assertEqual(max_storage_area([2, 1]), 2)

    def test_large_peak_middle(self):
        self.assertEqual(max_storage_area([1, 3, 5, 9, 5, 3, 1]), 15)  # width=7, height=3

if __name__ == '__main__':
    unittest.main()
