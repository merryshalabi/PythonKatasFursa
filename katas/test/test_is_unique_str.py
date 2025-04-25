import unittest
from katas.is_unique_str import is_unique


class TestIsUniqueStr(unittest.TestCase):
    def test_unique_str(self):
        self.assertEqual(is_unique("abd"), True)

    def test_not_unique_str(self):
        self.assertEqual(is_unique("aabbdes"), False)

    def test_empty_str(self):
        self.assertEqual(is_unique(""), True)

    def test_non_letter_duplicates(self):
        self.assertEqual(is_unique("123123"), True)



