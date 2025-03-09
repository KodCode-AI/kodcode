from solution import *

from solution import min_path_sum, TreeNode

# Constructing the tree:
#       10
#      /  \
#    10    20
#   /  \    \
# 2    20    13
def create_tree():
    two = TreeNode(2)
    twenty = TreeNode(20)
    ten_left = TreeNode(10, two, twenty)
    twenty_right = TreeNode(20)
    root = TreeNode(10, ten_left, twenty_right)
    twenty_right_right = TreeNode(13)
    twenty_right.right = twenty_right_right
    return root

def test_min_path_sum():
    root = create_tree()
    assert min_path_sum(root) == 42

def test_min_path_sum_single_node():
    root = TreeNode(10)
    assert min_path_sum(root) == 10

def test_min_path_sum_complex_tree():
    two = TreeNode(2)
    twenty_right_right = TreeNode(13)
    twenty_right = TreeNode(20, None, twenty_right_right)
    twenty_left = TreeNode(20)
    ten_left = TreeNode(10, two, twenty_left)
    root = TreeNode(10, ten_left, twenty_right)
    assert min_path_sum(root) == 45