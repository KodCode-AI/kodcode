from solution import *

import pytest

# Test helper functions and classes
def create_bst_from_list(arr):
    if not arr:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    for i, node in enumerate(nodes):
        if node:
            node.left = nodes[2 * i + 1] if 2 * i + 1 < len(nodes) else None
            node.right = nodes[2 * i + 2] if 2 * i + 2 < len(nodes) else None
    return nodes[0]

# Test cases
def test_kth_smallest_simple_tree():
    root = create_bst_from_list([3, 1, 4, None, 2])
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4

def test_kth_smallest_empty_tree():
    root = create_bst_from_list([])
    with pytest.raises(IndexError):
        kth_smallest(root, 1)

def test_kth_smallest_large_tree():
    root = create_bst_from_list([5, 3, 6, 2, 4, None, None, 1])
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4
    assert kth_smallest(root, 5) == 5
    assert kth_smallest(root, 6) == 6

def test_kth_smallest_single_node():
    root = create_bst_from_list([1])
    assert kth_smallest(root, 1) == 1

# Run the tests
def _run_tests():
    pytest.main([__file__])

if __name__ == "__main__":
    _run_tests()