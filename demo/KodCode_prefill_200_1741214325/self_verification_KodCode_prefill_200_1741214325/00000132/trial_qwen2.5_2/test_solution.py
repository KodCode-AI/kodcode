from solution import *

from solution import diameter_of_binary_tree, TreeNode

def create_tree(*values):
    """Helper function to create a binary tree from values."""
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def test_diameter_of_binary_tree():
    # Construct a tree
    tree = create_tree(1, 2, 3, 4, 5)
    assert diameter_of_binary_tree(tree) == 3

    # Construct another tree
    tree = create_tree(1, 2, 3, None, 4, 5)
    assert diameter_of_binary_tree(tree) == 4

    # Perfect binary tree
    tree = create_tree(1, 2, 3, 4, 5, 6)
    assert diameter_of_binary_tree(tree) == 5

    # A tree with a single node
    assert diameter_of_binary_tree(TreeNode(1)) == 0

    # A tree with no nodes
    assert diameter_of_binary_tree(None) == 0