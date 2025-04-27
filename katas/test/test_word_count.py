import unittest
from katas.word_count import count_words


class TestWordCount(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("This is a sample sentence for counting words."), 8)

    def test_empty_count_words(self):
        self.assertEqual(count_words(""),0)

    def test_spaces_only_count_words(self):
        self.assertEqual(count_words("  "),0)

    def test_more_than_one_space(self):
        self.assertEqual(count_words("this  is a sample  sentence for   counting  words"), 8)

