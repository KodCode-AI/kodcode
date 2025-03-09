from solution import *

def test_circular_array():
    circ_arr = CircularArray(4)
    assert circ_arr.to_string() == '[0, 0, 0, 0]'
    circ_arr.set(0, 1)
    assert circ_arr.to_string() == '[1, 0, 0, 0]'
    circ_arr.set(3, 2)
    assert circ_arr.to_string() == '[1, 0, 0, 2]'
    circ_arr.increment(0, 3)
    assert circ_arr.to_string() == '[4, 0, 0, 2]'
    circ_arr.increment(4, 1)
    assert circ_arr.to_string() == '[0, 1, 0, 2]'
    circ_arr.increment(-2, 3)
    assert circ_arr.to_string() == '[3, 1, 0, 2]'
    assert circ_arr.get(0) == 3
    assert circ_arr.get(2) == 0
    assert circ_arr.get(-1) == 2
    assert circ_arr.get(5) == 1

# Run tests using pytest
test_circular_array()