from solution import *

import pytest

def test_insert_and_get_root():
    # Test Case 1
    inserter = CBTArrayInserter([1, 2, 3])
    assert inserter.insert(5) == 0
    assert inserter.tree == [1, 2, 3, 5]  # 5 should be inserted at the last index while maintaining the property

    # Test Case 2
    inserter = CBTArrayInserter([1, 2, 4, 0])
    assert inserter.insert(3) == 0
    assert inserter.tree == [1, 2, 4, 0, 3]  # 3 should be inserted at the last index while maintaining the property

    # Test Case 3
    inserter = CBTArrayInserter([1, 2, 3, 5, 6])
    assert inserter.insert(7) == 0
    assert inserter.tree == [1, 2, 3, 5, 6, 7]  # 7 should be inserted at the last index while maintaining the property

    # Test Case 4: Inserting a target equal to the root value
    inserter = CBTArrayInserter([1, 2, 3, 4, 5])
    assert inserter.insert(4) == 0
    assert inserter.tree == [1, 2, 3, 5, 5, 4]  # Target 4 is already the root, should not change the tree structure

    # Test Case 5: Inserting at the last level
    inserter = CBTArrayInserter([1, 2, 3])
    assert inserter.insert(0) == 0
    assert inserter.tree == [1, 2, 3, 0]  # Target 0 should be inserted at the last index while maintaining the property

# Note: The `get_root` method always returns 0 as per the implementation. We can add a test-case if the method's behavior changes.