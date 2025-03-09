from solution import *

def test_find_non_repeated():
    assert find_non_repeated([2, 3, 4, 3, 5]) == 0
    assert find_non_repeated([1, 2, 2, 3, 4, 4, 5]) == 0
    assert find_non_repeated([6, 7, 8, 8, 9, 9]) == 0
    assert find_non_repeated([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 7
    assert find_non_repeated([1, 1, 2, 2]) == -1
    assert find_non_repeated([7]) == 0
    assert find_non_repeated([]) == -1

# Edge cases
def test_find_non_repeated_edge_cases():
    assert find_non_repeated([1, 1, 1, 2]) == 3
    assert find_non_repeated([1, 2, 1, 3, 3, 4, 4]) == 1
    assert find_non_repeated([1, 2, 2, 3]) == 0