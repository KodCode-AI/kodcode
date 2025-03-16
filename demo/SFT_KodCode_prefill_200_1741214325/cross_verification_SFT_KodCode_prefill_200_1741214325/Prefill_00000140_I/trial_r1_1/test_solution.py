from solution import *

def test_find_index_of_five():
    assert find_index_of_five([1, 2, 3, 4, 5, 6]) == 4
    assert find_index_of_five([1, 5, 2, 3, 4, 6]) == 1
    assert find_index_of_five([1, 2, 3, 4, 6]) == -1
    assert find_index_of_five([5, 1, 2, 3, 4, 6]) == 0
    assert find_index_of_five([]) == -1