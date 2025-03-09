from solution import *

import pytest

def test_find_longest_recurring_cycle():
    assert find_longest_recurring_cycle(10) == 7
    assert find_longest_recurring_cycle(100) == 97
    assert find_longest_recurring_cycle(1000) == 983
    assert find_longest_recurring_cycle(50) == 49
    assert find_longest_recurring_cycle(20) == 19
    assert find_longest_recurring_cycle(30) == 29
    assert find_longest_recurring_cycle(70) == 67

pytest.main(['-v', '-s', 'test_find_longest_recurring_cycle.py'])