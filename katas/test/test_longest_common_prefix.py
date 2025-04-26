import unittest
from katas.longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    def test_common_prefix(self):
        words = ["abc" , "abcd" , "ab"]
        self.assertEqual(longest_common_prefix(words), "ab")

    def test_no_common_prefix(self):
        words = ["abc" , "def" , "ghi"]
        self.assertEqual(longest_common_prefix(words), "")

    def test_one_word_prefix(self):
        words = ["abc"]
        self.assertEqual(longest_common_prefix(words), "abc")

    def test_empty_common_prefix(self):
        words = [""]
        self.assertEqual(longest_common_prefix(words), "")


