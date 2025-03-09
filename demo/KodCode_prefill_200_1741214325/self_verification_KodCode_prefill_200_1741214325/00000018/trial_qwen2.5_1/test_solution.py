from solution import *

from solution import minimal_path_sum, TreeNode

def create_tree(*vals):
    def add_node(index, val):
        if not tree[index]:
            tree[index] = TreeNode()
        if val is not None:
            tree[index].val = val
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < len(tree):
            add_node(left_index, vals[left_index])
        if right_index < len(tree):
            add_node(right_index, vals[right_index])
    tree = [None] * 20
    add_node(0, None)
    for i, val in enumerate(vals):
        if val is not None:
            add_node(i, val)
    return tree[0]

def test_minimal_path_sum():
    # Create a binary tree
    root = create_tree(
        60, 20, 80, 40, 50, None, 100, None, 65
    )
    assert minimal_path_sum(root) == 180

    # Create another binary tree
    root2 = create_tree(
        10, 20, 20, 30, 40, 30, 50
    )
    assert minimal_path_sum(root2) == 50

    # Create a binary tree with negative values
    root3 = create_tree(
        -6, -2, -8, -10, -4
    )
    assert minimal_path_sum(root3) == -18

    # Create a binary tree with a single root node
    root4 = create_tree(1)
    assert minimal_path_sum(root4) == 1

    # Create a binary tree with all leaves at the same level
    root5 = create_tree(
        2, 3, 7, 8, 4, 5, None, None, 1
    )
    assert minimal_path_sum(root5) == 11

# The following lines are for the test functions
# and would be executed when running the script
# directly.
if __name__ == "__main__":
    test_minimal_path_sum()