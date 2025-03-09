from solution import *

from solution import TreeNode, find_paths

def test_find_paths_simple_target():
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1))))
    target = 22
    expected = [[5, 4, 11, 2], [5, 8, 4, 1]]
    assert sorted(find_paths(root, target, 0)) == expected

def test_find_paths_without_target():
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1))))
    target = 21
    assert find_paths(root, target, 0) == []