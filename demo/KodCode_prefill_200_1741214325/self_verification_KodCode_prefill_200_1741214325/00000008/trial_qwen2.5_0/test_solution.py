from solution import *

from solution import max_without_if_else

def test_max_without_if_else():
    assert max_without_if_else(1, 2) == 2
    assert max_without_if_else(3, 1) == 3
    assert max_without_if_else(-1, -2) == -1
    assert max_without_if_else(-3, 1) == 1
    assert max_without_if_else(3, -2) == 3
    assert max_without_if_else(0, 0) == 0
    assert max_without_if_else(-3, -3) == -3