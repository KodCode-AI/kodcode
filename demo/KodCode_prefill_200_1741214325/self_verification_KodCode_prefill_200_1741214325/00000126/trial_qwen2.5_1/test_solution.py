from solution import *

def test_is_ascending():
    assert is_ascending([1, 2, 3, 4, 5]) == True
    assert is_ascending([10, 20, 20, 30, 40]) == True
    assert is_ascending([5, 4, 3, 2, 1]) == False
    assert is_ascending([1, 2, 3, 3, 4, 5]) == True
    assert is_ascending([1, 2, 3, 5, 4]) == False
    assert is_ascending([]) == True
    assert is_ascending([7]) == True
    assert is_ascending([1, 3, 2]) == False