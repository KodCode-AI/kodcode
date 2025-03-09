from solution import *

from solution import count_smaller

def test_count_smaller():
    assert count_smaller([6, 5, 4, 8]) == [2, 1, 1, 3]
    assert count_smaller([2, 0, 1]) == [1, 0, 0]
    assert count_smaller([10, 10, 10, 0, 0]) == [0, 0, 0, 1, 2]
    assert count_smaller([1]) == [0]
    assert count_smaller([3, 2, 1, 0, 4, 5]) == [1, 1, 1, 0, 3, 4]