from solution import *

def test_count_ways():
    assert count_ways(5) == 2  # Because 5 can be represented as 2 + 3 or 5 itself
    assert count_ways(9) == 3  # Because 9 can be represented as 4 + 5, 2 + 3 + 4, or 9 itself
    assert count_ways(15) == 4  # Because 15 can be represented as 1 + 2 + 3 + 4 + 5, 7 + 8, 4 + 5 + 6, or 15 itself
    assert count_ways(1) == 1  # 1 can only be represented as 1
    assert count_ways(10) == 2  # Because 10 can be represented as 1 + 2 + 3 + 4 or 5 + 5