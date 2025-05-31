import unittest

from katas.is_valid_git_tree import is_valid_git_tree  # Replace with actual module name if needed

class TestIsValidGitTree(unittest.TestCase):

    def test_valid_tree(self):
        tree = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": [],
            "D": []
        }
        self.assertTrue(is_valid_git_tree(tree))

    def test_cycle_tree(self):
        tree = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"]
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_multiple_roots(self):
        tree = {
            "A": ["B"],
            "C": ["D"]
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_disconnected_node(self):
        tree = {
            "A": ["B"],
            "B": [],
            "C": []  # disconnected node
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_self_loop(self):
        tree = {
            "A": ["A"]
        }
        self.assertFalse(is_valid_git_tree(tree))

    def test_single_node(self):
        tree = {
            "A": []
        }
        self.assertTrue(is_valid_git_tree(tree))

    def test_empty_tree(self):
        tree = {}
        self.assertFalse(is_valid_git_tree(tree))  # No root

if __name__ == "__main__":
    unittest.main()
