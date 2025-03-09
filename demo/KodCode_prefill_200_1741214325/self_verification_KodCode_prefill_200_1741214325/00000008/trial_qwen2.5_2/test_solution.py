from solution import *

from solution import max_without_conditions

def test_max_without_conditions():
    assert max_without_conditions(10, 20) == 20
    assert max_without_conditions(20, 10) == 20
    assert max_without_conditions(-5, 5) == 5
    assert max_without_conditions(-5, -10) == -5
    assert max_without_conditions(0, 0) == 0