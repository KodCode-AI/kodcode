from solution import *

from solution import min_operations_to_equal_elements

def test_min_operations_to_equal_elements():
    assert min_operations_to_equal_elements([1, 2, 3]) == 2  # [1, 2, 3] -> [2, 2, 2] (2 operations)
    assert min_operations_to_equal_elements([1, 1, 1]) == 0  # All elements are already equal
    assert min_operations_to_equal_elements([1, 10, 100]) == 110  # [1, 10, 100] -> [50, 50, 50] (110 operations)
    assert min_operations_to_equal_elements([5, 5, 3, 3]) == 4  # [5, 5, 3, 3] -> [4, 4, 4, 4] or [5, 5, 5, 5] (4 operations)