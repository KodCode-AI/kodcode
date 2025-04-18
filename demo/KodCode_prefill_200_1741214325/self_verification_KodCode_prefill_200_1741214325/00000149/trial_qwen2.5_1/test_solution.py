from solution import *

from solution import min_operations_to_equal_elements

def test_min_operations_to_equal_elements():
    assert min_operations_to_equal_elements([1, 2, 3]) == 2
    assert min_operations_to_equal_elements([1, 1, 1]) == 0
    assert min_operations_to_equal_elements([1, 10, 100]) == 189
    assert min_operations_to_equal_elements([5, 5, 5, 5]) == 0
    assert min_operations_to_equal_elements([0, 2, 4]) == 4