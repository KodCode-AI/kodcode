from solution import *

from solution import count_ways_to_sum_consecutively

def test_count_ways_to_sum_consecutively():
    assert count_ways_to_sum_consecutively(5) == 2  # 1+4 or 2+3
    assert count_ways_to_sum_consecutively(9) == 3  # 4+5, 2+3+4, 1+2+3+3
    assert count_ways_to_sum_consecutively(15) == 4  # 1+2+3+4+5, 8+7, 4+5+6, 1+2+3+4+5
    assert count_ways_to_sum_consecutively(1) == 1  # 1
    assert count_ways_to_sum_consecutively(3) == 1  # 1+2
    assert count_ways_to_sum_consecutively(16) == 1  # No way to represent 16 as sum of consecutive positive integers