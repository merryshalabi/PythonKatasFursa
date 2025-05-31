from itertools import cycle
from os import MFD_ALLOW_SEALING


def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise
    """
    all_nodes = set(tree_map.keys())
    all_child_nodes = set()

    for children in tree_map.values():
        for child in children:
            all_child_nodes.add(child)

    root = all_nodes - all_child_nodes
    if len(root) != 1 :
        return False

    start = root.pop()

    global_visited = set()

    def dfs(node,visited):
        if node in visited:
            return False
        if node in global_visited:
            return True
        visited.add(node)

        for child in tree_map.get(node,[]):
            if child in visited:
                return False
            else:
                dfs(node,visited)

        visited.remove(node)
        global_visited.add(node)
        return True

    visited = set()
    if not dfs(start,visited):
        return False


    return True


if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False