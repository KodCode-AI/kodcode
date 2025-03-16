from solution import *

from solution import single_number

def test_single_number():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([8]) == 8
    assert single_number([7, 3, 5, 3, 7, 5, 6]) == 6