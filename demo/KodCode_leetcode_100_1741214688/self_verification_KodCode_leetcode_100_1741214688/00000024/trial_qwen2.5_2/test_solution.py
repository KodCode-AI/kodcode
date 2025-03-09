from solution import *

from solution import TreeNode, kthSmallest

def test_kthSmallest_case1():
    # Construct the example tree
    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    
    node5.left = node3
    node5.right = node6
    node3.left = node2
    node3.right = node4
    
    assert kthSmallest(node5, 3) == 3

def test_kthSmallest_case2():
    node1 = TreeNode(1)
    assert kthSmallest(node1, 1) == 1

def test_kthSmallest_case3():
    node4 = TreeNode(4)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4.left = node2
    node4.right = node5
    node2.left = node1
    node2.right = node3
    
    assert kthSmallest(node4, 1) == 1
    assert kthSmallest(node4, 3) == 3

def test_kthSmallest_case4():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node2.left = node1
    node2.right = node3
    
    assert kthSmallest(node2, 2) == 2