from solution import *

def test_fibonacci_up_to_n():
    assert fibonacci_up_to_n(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci_up_to_n(1) == [0, 1]
    assert fibonacci_up_to_n(0) == []
    assert fibonacci_up_to_n(20) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert fibonacci_up_to_n(5) == [0, 1, 1, 2, 3, 5]