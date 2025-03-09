from solution import *

``
def test_calculate_difference():
    assert calculate_difference(10) == 2640
    assert calculate_difference(15) == 13160
    assert calculate_difference(20) == 41230
    assert calculate_difference(50) == 1582700
    assert calculate_difference(1) == 0
    assert calculate_difference(1000000) == 2533335000000

test_calculate_difference()