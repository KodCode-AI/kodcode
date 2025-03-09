from solution import *

from solution import CircularArray

def test circular_array():
    arr = CircularArray(5)
    assert arr.to_string() == '[0,0,0,0,0]'
    arr.set(3, 4)
    assert arr.to_string() == '[0,0,0,4,0]'
    arr.set(10, 5)
    assert arr.to_string() == '[0,5,0,4,0]'
    arr.increment(1, 7)
    assert arr.to_string() == '[0,12,0,4,0]'
    arr.increment(10, 2)
    assert arr.to_string() == '[0,14,0,4,0]'
    arr.increment(-1, 3)
    assert arr.to_string() == '[3,14,0,4,0]'
    arr.increment(-6, 3)
    assert arr.to_string() == '[3,14,0,4,3]'
    arr.increment(8, -2)
    assert arr.to_string() == '[3,12,0,4,3]'
    arr.increment(-9, -1)
    assert arr.to_string() == '[3,11,0,4,3]'
    arr.set(-2, 1)
    assert arr.to_string() == '[1,11,0,4,3]'
    arr.set(6, 2)
    assert arr.to_string() == '[1,11,0,4,2]'