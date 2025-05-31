import unittest
from collections import Counter
from katas.test_case_grouping import group_test_cases  # Adjust the import path as needed


def is_valid_grouping(group_sizes, result):
    seen = []
    for group in result:
        size = group_sizes[group[0]]
        if any(group_sizes[i] != size for i in group):
            return False
        if len(group) != size:
            return False
        seen.extend(group)
    return Counter(seen) == Counter(range(len(group_sizes)))


class TestGroupTestCases(unittest.TestCase):
    def test_example_case(self):
        input_data = [1, 2, 3, 3, 3, 2]
        result = group_test_cases(input_data)
        self.assertTrue(is_valid_grouping(input_data, result))

    def test_all_single(self):
        input_data = [1, 1, 1, 1]
        result = group_test_cases(input_data)
        self.assertEqual(sorted(result), [[0], [1], [2], [3]])
        self.assertTrue(is_valid_grouping(input_data, result))

    def test_all_same_size(self):
        input_data = [2, 2, 2, 2]
        result = group_test_cases(input_data)
        self.assertTrue(is_valid_grouping(input_data, result))
        self.assertEqual(len(result), 2)  # Two groups of size 2

    def test_mixed_case(self):
        input_data = [2, 2, 1, 1]
        result = group_test_cases(input_data)
        self.assertTrue(is_valid_grouping(input_data, result))

    def test_single_group(self):
        input_data = [4, 4, 4, 4]
        result = group_test_cases(input_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], [0, 1, 2, 3])
        self.assertTrue(is_valid_grouping(input_data, result))

    def test_long_input(self):
        input_data = [3]*9
        result = group_test_cases(input_data)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(len(group) == 3 for group in result))
        self.assertTrue(is_valid_grouping(input_data, result))

    def test_invalid_input(self):
        input_data = [1, 2, 2]
        result = group_test_cases(input_data)
        self.assertTrue(is_valid_grouping(input_data, result))  # Should still be valid

    def test_empty_input(self):
        self.assertEqual(group_test_cases([]), [])


if __name__ == "__main__":
    unittest.main()
