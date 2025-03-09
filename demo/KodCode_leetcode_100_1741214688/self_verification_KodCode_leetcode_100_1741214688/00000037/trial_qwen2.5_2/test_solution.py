from solution import *

def test_min_intervals_to_remove():
    assert min_intervals_to_remove([[1,2], [2,3], [3,4], [1,3]]) == 1, "Test case 1 failed"
    assert min_intervals_to_remove([[1,2], [1,2], [1,2]]) == 2, "Test case 2 failed"
    assert min_intervals_to_remove([[1,2], [2,3]]) == 0, "Test case 3 failed"
    assert min_intervals_to_remove([[1,10], [2,3], [4,5], [6,7], [8,9],[1,1],[2,2]]) == 5, "Test case 4 failed"
    assert min_intervals_to_remove([]) == 0, "Test case 5 failed"

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])