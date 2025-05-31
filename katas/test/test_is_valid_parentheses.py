import unittest
from katas.is_valid_parentheses import is_valid_parentheses  # adjust if needed

class TestIsValidParentheses(unittest.TestCase):

    def test_valid_simple(self):
        self.assertTrue(is_valid_parentheses("()"))
        self.assertTrue(is_valid_parentheses("[]"))
        self.assertTrue(is_valid_parentheses("{}"))

    def test_valid_combined(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertTrue(is_valid_parentheses("{[]()}"))

    def test_invalid_mismatch(self):
        self.assertFalse(is_valid_parentheses("(]"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertFalse(is_valid_parentheses("{[}"))  # opened with [ closed with }

    def test_incomplete_open(self):
        self.assertFalse(is_valid_parentheses("("))
        self.assertFalse(is_valid_parentheses("[{"))

    def test_incomplete_close(self):
        self.assertFalse(is_valid_parentheses(")]"))
        self.assertFalse(is_valid_parentheses("}"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parentheses(""))

    def test_extra_characters(self):
        self.assertTrue(is_valid_parentheses("{[()]}"))
        self.assertFalse(is_valid_parentheses("{[a+b]*2}-3)"))

if __name__ == '__main__':
    unittest.main()
