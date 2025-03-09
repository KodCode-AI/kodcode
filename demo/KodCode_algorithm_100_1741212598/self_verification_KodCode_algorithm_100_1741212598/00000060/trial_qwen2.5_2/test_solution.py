from solution import *

import pytest

def test_diophantine_all_values():
    assert diophantine_all_values(2, 3, 5, 5) == [(-5, 5), (-4, 3), (-3, 1), (1, -4), (3, -2), (5, -1)]
    assert diophantine_all_values(6, 9, 3, 10) == []
    assert diophantine_all_values(1, 1, 2, 10) == [(0, 2), (2, 0), (-2, -2), (1, 1), (-1, -1), (-1, 0)]
    assert diophantine_all_values(5, 7, 25, 10) == [(5, -0)]
    assert diophantine_all_values(10, 15, 50, 10) == [(0, 4), (1, 2)]