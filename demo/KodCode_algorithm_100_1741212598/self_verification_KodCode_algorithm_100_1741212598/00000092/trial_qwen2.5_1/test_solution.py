from solution import *

import pytest

def test_find_longest_recurring_cycle():
    assert find_longest_recurring_cycle(10) == 7
    assert find_longest_recurring_cycle(100) == 97
    assert find_longest_recurring_cycle(1000) == 983
    assert find_longest_recurring_cycle(15) == 7
    assert find_longest_recurring_cycle(20) == 19
    assert find_longest_recurring_cycle(50) == 49

def test_edge_cases():
    with pytest.raises(AssertionError):
        find_longest_recurring_cycle(1)
    with pytest.raises(AssertionError):
        find_longest_recurring_cycle(1001)