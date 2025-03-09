from solution import *

def setup_tree():
    root = TreeNode(5)
    root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    root.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
    return root

def test_find_paths():
    root = setup_tree()
    target = 22
    expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert find_paths(root, target) == expected

def test_no_paths():
    root = setup_tree()
    target = 100  # No path in the tree has a sum of 100 or more
    expected = []
    assert find_paths(root, target) == expected

def test_single_node_tree():
    root = TreeNode(5)
    target = 5
    expected = [[5]]
    assert find_paths(root, target) == expected