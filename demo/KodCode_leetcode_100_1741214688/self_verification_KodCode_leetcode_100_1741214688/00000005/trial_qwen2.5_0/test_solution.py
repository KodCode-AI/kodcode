from solution import *

from solution import sumNumbers, TreeNode

def setup_tree(lvl, idx):
    if idx >= 2**lvl:  # Stop when reached impossible index
        return None
    node = TreeNode(idx % 10)
    node.left = setup_tree(lvl, 2*idx + 1)
    node.right = setup_tree(lvl, 2*idx + 2)
    return node

def test_sumNumbers():
    assert sumNumbers(None) == 0  # Empty tree
    assert sumNumbers(TreeNode(1)) == 1  # Single node tree
    assert sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25  # Binary tree: 12 + 13 = 25
    assert sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))) == 1026  # More complex binary tree: 495 + 491 + 40 = 1026
    tree = setup_tree(4, 0)  # Full binary tree of level 4, replacing all leafs with their values
    expected_sum = 0
    for i in range(2**4):
        expected_sum += int(str(i), 4) * 4**4  # Convert i to base 4 and shift left by 4 places
    assert sumNumbers(tree) == expected_sum  # Check the sum of all root-to-leaf numbers in a full binary tree