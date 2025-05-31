import unittest
from katas.sliding_window_maximum import max_sliding_window  # Adjust import path as needed

class TestMaxSlidingWindow(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(
            max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7]
        )

    def test_window_size_1(self):
        self.assertEqual(
            max_sliding_window([1, -1], 1),
            [1, -1]
        )

    def test_window_size_2(self):
        self.assertEqual(
            max_sliding_window([9, 11, 3, 4, 8, 7], 2),
            [11, 11, 4, 8, 8]
        )

    def test_entire_window(self):
        self.assertEqual(
            max_sliding_window([1, 3, 2], 3),
            [3]
        )

    def test_window_size_equals_list_length(self):
        self.assertEqual(
            max_sliding_window([5, 2, 1, 3, 4], 5),
            [5]
        )

    def test_empty_list(self):
        self.assertEqual(
            max_sliding_window([], 3),
            []
        )

    def test_zero_window(self):
        self.assertEqual(
            max_sliding_window([1, 2, 3], 0),
            []
        )

    def test_single_element(self):
        self.assertEqual(
            max_sliding_window([5], 1),
            [5]
        )

    def test_repeated_elements(self):
        self.assertEqual(
            max_sliding_window([2, 2, 2, 2], 2),
            [2, 2, 2]
        )

if __name__ == "__main__":
    unittest.main()
