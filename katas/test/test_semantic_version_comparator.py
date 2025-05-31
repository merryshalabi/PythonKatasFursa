import unittest
from katas.semantic_version_comparator import compare_versions  # Adjust the import path as needed

class TestCompareVersions(unittest.TestCase):
    def test_equal_versions(self):
        self.assertEqual(compare_versions("1.2.3", "1.2.3"), 0)
        self.assertEqual(compare_versions("1.2", "1.2.0"), 0)
        self.assertEqual(compare_versions("1", "1.0.0"), 0)

    def test_version1_less_than_version2(self):
        self.assertEqual(compare_versions("1.0.0", "1.0.1"), -1)
        self.assertEqual(compare_versions("1.2", "1.2.1"), -1)
        self.assertEqual(compare_versions("0.9.9", "1.0.0"), -1)
        self.assertEqual(compare_versions("2.0.0", "10.0.0"), -1)

    def test_version1_greater_than_version2(self):
        self.assertEqual(compare_versions("2.1.0", "1.9.9"), 1)
        self.assertEqual(compare_versions("1.10.0", "1.2.0"), 1)
        self.assertEqual(compare_versions("1.0.0", "0.9.9"), 1)

    def test_missing_patch(self):
        self.assertEqual(compare_versions("1.0", "1.0.0"), 0)
        self.assertEqual(compare_versions("1.0.1", "1.0"), 1)
        self.assertEqual(compare_versions("1.0", "1.0.1"), -1)

    def test_missing_minor_and_patch(self):
        self.assertEqual(compare_versions("1", "1.0.0"), 0)
        self.assertEqual(compare_versions("1.1", "1"), 1)
        self.assertEqual(compare_versions("1", "1.1"), -1)

if __name__ == "__main__":
    unittest.main()
