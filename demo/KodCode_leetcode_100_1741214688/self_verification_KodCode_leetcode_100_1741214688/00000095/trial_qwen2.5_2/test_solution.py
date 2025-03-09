from solution import *

from solution import TreeNode, can_partition_bst

def test_can_partition_bst():
    # Constructing a simple BST
    #       1
    #        \
    #         2
    #        /
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    assert not can_partition_bst(root)

    # Constructing a balanced BST
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    assert can_partition_bst(root)

# Constructing a BST where the sum of the values cannot be partitioned into two equal subsets
#       1
#        \
#         2
#        /
#       4
#      /
#     8
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.left.left = TreeNode(8)

    assert not can_partition_bst(root)