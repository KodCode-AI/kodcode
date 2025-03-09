from solution import *

from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def vertical_order_tester():
    # Creating the tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    expected_output = [[9], [3, 15], [20], [7]]
    assert vertical_order(root) == expected_output

    # Creating another tree
    root2 = None
    expected_output2 = []
    assert vertical_order(root2) == expected_output2

    # Another tree with a single root node
    root3 = TreeNode(1)
    expected_output3 = [[1]]
    assert vertical_order(root3) == expected_output3

    # Tree with nodes in a single column
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    expected_output4 = [[4], [2], [1], [3], [5]]
    assert vertical_order(root4) == expected_output4

vertical_order_tester()