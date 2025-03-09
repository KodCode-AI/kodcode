from solution import *

def test_find_common_elements():
    assert find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert find_common_elements(['apple', 'banana', 'cherry'], ['banana', 'date', 'fig']) == ['banana']
    assert find_common_elements([], [1, 2, 3]) == []
    assert find_common_elements([1, 2, 3], []) == []
    assert find_common_elements([10, 20, 30], [10, 40, 50]) == [10]