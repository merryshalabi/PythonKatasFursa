import unittest
from typing import List
from katas.requirements_coverage import select_minimal_test_cases  # Update import path as needed

class TestSelectMinimalTestCases(unittest.TestCase):

    def assertValidCover(self, test_cases: List[List[int]], selected_indices: List[int]):
        all_requirements = set(req for tc in test_cases for req in tc)
        selected_reqs = set()
        for i in selected_indices:
            selected_reqs.update(test_cases[i])
        self.assertEqual(selected_reqs, all_requirements)

    def test_example_case(self):
        test_cases = [
            [1, 2, 3],
            [1, 4],
            [2, 3, 4],
            [1, 5],
            [3, 5]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(result, [[2, 3]])  # Accept only minimal optimal solution
        self.assertValidCover(test_cases, result)

    def test_single_test_case(self):
        test_cases = [
            [1, 2, 3, 4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [0])

    def test_no_overlap(self):
        test_cases = [
            [1],
            [2],
            [3]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertCountEqual(result, [0, 1, 2])

    def test_minimal_two(self):
        test_cases = [
            [1, 2],
            [2, 3],
            [1, 3]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertIn(result, [[0, 1], [1, 2], [0, 2]])
        self.assertValidCover(test_cases, result)

    def test_large_case(self):
        test_cases = [
            [1], [2], [3], [4],
            [1, 2, 3, 4]
        ]
        result = select_minimal_test_cases(test_cases)
        self.assertEqual(result, [4])


if __name__ == '__main__':
    unittest.main()
