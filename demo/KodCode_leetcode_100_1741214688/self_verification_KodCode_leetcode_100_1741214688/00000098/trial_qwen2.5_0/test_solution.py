from solution import *

import pytest

def test_cbt_array_inserter():
    def check_tree(root, expected_tree):
        tree = [None] * (len(expected_tree) + 1)
        inserter = CBTArrayInserter(tree)
        for val in expected_tree:
            assert inserter.insert(val) == root
            assert inserter.get_root() == root
            root += 1
            expected_tree.append(val)

    # Example 1: Basic insertion and get_root checks
    check_tree(0, [1, 2, 3, 4, 5])

    # Example 2: Insertion with larger values and get_root checks
    check_tree(0, [23, 14, 21, 13, 4, 6, 7, 9, 22])

    # Example 3: Insertion with negative values and get_root checks
    check_tree(0, [0, -1, -2, -3, -4])

    # Example 4: Insertion with mixed values and get_root checks
    check_tree(0, [15, 10, 21, 22, 45, 19, 27, 28, 39, 40])

# This test runs multiple test cases
if __name__ == "__main__":
    pytest.main([__file__])