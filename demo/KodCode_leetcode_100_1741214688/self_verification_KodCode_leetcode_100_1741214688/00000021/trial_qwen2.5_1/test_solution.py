from solution import *

def setup_tree():
    """
    Helper function to create a test BST.
    """
    three = TreeNode(3)
    one = TreeNode(1)
    four = TreeNode(4)
    two = TreeNode(2, one, three)
    five = TreeNode(5)
    root = TreeNode(4, two, five, right=TreeNode(6, right=TreeNode(7)))
    return root

def test_kth_smallest():
    """
    Test for the kth smallest element function.
    """
    root = setup_tree()
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4
    assert kth_smallest(root, 5) == 5
    assert kth_smallest(root, 6) == 6
    assert kth_smallest(root, 7) == 7

def test_single_node_tree():
    """
    Test for a tree with a single node.
    """
    root = TreeNode(5)
    assert kth_smallest(root, 1) == 5

# Adding further test cases to edge cases
def test_no_left_subtree():
    """
    Test for a tree where the left subtree is empty.
    """
    root = TreeNode(4, right=TreeNode(6, TreeNode(7)))
    assert kth_smallest(root, 1) == 4
    assert kth_smallest(root, 2) == 6
    assert kth_smallest(root, 3) == 7

# Run tests
test_kth_smallest()
test_single_node_tree()
test_no_left_subtree()