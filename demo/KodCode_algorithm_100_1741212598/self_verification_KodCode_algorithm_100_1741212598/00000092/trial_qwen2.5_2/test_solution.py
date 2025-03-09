from solution import *

import pytest

def test_find_longest_recurring_cycle():
    assert find_longest_recurring_cycle(10) == 7
    assert find_longest_recurring_cycle(100) == 97
    assert find_longest_recurring_cycle(1000) == 983

def test_smaller_denominator_limit():
    assert find_longest_recurring_cycle(1) == None  # No valid denominator in this range
    assert find_longest_recurring_cycle(2) == 1  # Only 1 valid denominator, no recurring cycle

def test_edge_cases():
    assert find_longest_recurring_cycle(3) == 2  # 1/2 and 1/3 are considered, 1/3 has a cycle but 2 is smaller

def test_large_denominator_limit():
    assert find_longest_recurring_cycle(1001) == 983  # Test beyond the specified limit to ensure handling

def test_multiples_of_2_and_5():
    assert find_longest_recurring_cycle(15) == 13  # Skip multiples of 2 and 5

def test_performance():
    assert find_longest_recurring_cycle(1000) == 983  # Performance check, should be efficient