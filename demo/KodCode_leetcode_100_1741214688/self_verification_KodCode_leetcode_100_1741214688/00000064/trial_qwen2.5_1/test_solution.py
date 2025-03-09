from solution import *

from solution import TreeNode, find_target, insert

def test_find_target_exist():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    assert find_target(root, 3) == True
    assert find_target(root, 5) == True
    assert find_target(root, 7) == True

def test_find_target_not_exist():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    assert find_target(root, 0) == False
    assert find_target(root, 8) == False

def test_insert():
    root = None
    root = insert(root, 4)
    root = insert(root, 2)
    root = insert(root, 6)
    root = insert(root, 1)
    root = insert(root, 3)
    root = insert(root, 5)
    root = insert(root, 7)
    assert find_target(root, 2) == True
    assert find_target(root, 6) == True
    assert find_target(root, 1) == True
    assert find_target(root, 3) == True
    assert find_target(root, 5) == True
    assert find_target(root, 7) == True
    assert find_target(root, 0) == False
    assert find_target(root, 8) == False