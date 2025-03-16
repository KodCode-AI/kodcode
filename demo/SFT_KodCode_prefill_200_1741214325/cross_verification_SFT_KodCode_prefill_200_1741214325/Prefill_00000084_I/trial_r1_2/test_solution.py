from solution import *

from solution import count_value_occurrences

def test_count_value_occurrences():
    assert count_value_occurrences([1, 2, 3, 4, 5, 2, 2, 3], 2) == 3
    assert count_value_occurrences([1, 2, 3, 4, 5, 2, 2, 3], 7) == 0
    assert count_value_occurrences([1, 1, 1, 1, 1], 1) == 5
    assert count_value_occurrences([], 3) == 0