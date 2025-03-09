from solution import *

from solution import TreeNode, mirror_tree

def test_mirror_tree():
    # Construct a simple tree
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    # Expected output after mirroring
    #       1
    #      / \
    #     3   2
    #        / \
    #       6   4
    #          /
    #         5
    mirrored_root = mirror_tree(root)
    
    assert mirrored_root.left.value == 3
    assert mirrored_root.right.left.value == 6
    assert mirrored_root.right.right.value == 4
    assert mirrored_root.right.right.right.value == 5