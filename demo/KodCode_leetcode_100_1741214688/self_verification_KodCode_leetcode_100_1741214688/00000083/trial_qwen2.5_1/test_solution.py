from solution import *

def test_k_smallest_abs_differences():
    assert k_smallest_abs_differences([1, 3, 1], 1) == [2]
    assert k_smallest_abs_differences([1, -1, -2, 2], 3) == [1, 1, 3]
    assert k_smallest_abs_differences([4, 2, 5, 3], 2) == [1, 3]
    assert k_smallest_abs_differences([8, 8, 8, 8], 2) == [0]
    
def test_k_smallest_abs_differences_edge_cases():
    assert k_smallest_abs_differences([1, 2, 3], 5) == [1]
    assert k_smallest_abs_differences([10], 1) == []
    assert k_smallest_abs_diffrences([]) == []