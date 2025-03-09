from solution import *

def test_cbt_array_inserter():
    tree = [1, 2, 3, 4, 5, 6, 7]
    inserter = CBTArrayInserter(tree)
    assert inserter.insert(8) == 0  # Insert a new node with value 8 at the end
    assert inserter.get_root() == 0  # The root index remains 0
    assert inserter.insert(9) == 0  # Insert a new node with value 9 at the end
    assert inserter.insert(10) == 0 # Insert a new node with value 10 at the end

    tree = [0, 1, 0, 0, 2, 3, 4, 5, 6, 7]
    inserter = CBTArrayInserter(tree)
    assert inserter.insert(8) == 0  # Insert a new node with value 8 at the end
    assert inserter.get_root() == 0  # The root index remains 0
    assert inserter.insert(9) == 0  # Insert a new node with value 9 at the end
    assert inserter.insert(10) == 0 # Insert a new node with value 10 at the end