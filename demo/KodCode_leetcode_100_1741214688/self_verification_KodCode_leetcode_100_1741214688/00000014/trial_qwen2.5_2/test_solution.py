from solution import *

from solution import sum_of_odd_parent_nodes, TreeNode

def create_tree(*vals):
    if not vals:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    for i, node in enumerate(nodes):
        if node:
            parent_idx = (i - 1) // 2
            if 2 * parent_idx + 1 <= i:
                node.left = nodes[2 * parent_idx + 1]
            if 2 * parent_idx + 2 <= i:
                node.right = nodes[2 * parent_idx + 2]
    return nodes[0]

def test_sum_of_odd_parent_nodes():
    # Example 1
    root = create_tree(6, 7, 8, 2, 7, 1, 3, None, None, None, 5, 4)
    assert sum_of_odd_parent_nodes(root) == 18
    
    # Example 2
    root = create_tree(15, 7)
    assert sum_of_odd_parent_nodes(root) == 0
    
    # Example 3
    root = create_tree(8, None, 10, None, 2, None, 1, None, None, None, 6)
    assert sum_of_odd_parent_nodes(root) == 12

    # Additional test case with no odd parent nodes
    root = create_tree(2, 3, 4)
    assert sum_of_odd_parent_nodes(root) == 0