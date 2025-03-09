from solution import *

from solution import TreeNode, path_sum

def test_path_sum():
    # Construct the tree:     5
    #                         / \
    #                        4   8
    #                       /   / \
    #                      11  13  4
    #                     /  \     \
    #                    7    2      1
    root = TreeNode(5, 
                    TreeNode(4, 
                             TreeNode(11, 
                                      TreeNode(7), 
                                      TreeNode(2)), 
                             None), 
                    TreeNode(8, 
                             TreeNode(13), 
                             TreeNode(4, 
                                      None, 
                                      TreeNode(1))))
    targetSum = 22

    expected = [[5, 4, 11, 2], [5, 8, 4, 1]]
    assert path_sum(root, targetSum) == expected

test_path_sum()