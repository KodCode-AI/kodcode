from solution import *

def test_fibonacci_up_to_n():
    assert fibonacci_up_to_n(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci_up_to_n(1) == [0, 1, 1]
    assert fibonacci_up_to_n(0) == [0]
    assert fibonacci_up_to_n(19) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert fibonacci_up_to_n(34) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_up_to_n(-1) == []