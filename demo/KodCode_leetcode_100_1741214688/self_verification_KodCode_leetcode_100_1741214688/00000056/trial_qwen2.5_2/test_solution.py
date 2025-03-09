from solution import *

from solution import max_distinct_elements

def test_max_distinct_elements():
    assert max_distinct_elements([1,2,3,2,2,1,3], 3) == 3
    assert max_distinct_elements([1,2,1,2,1,3,3], 3) == 2
    assert max_distinct_elements([1,2,1,3,4,3,1,2], 4) == 3
    assert max_distinct_elements([1,1,2,2,3,3,4,4,5,5], 5) == 5
    assert max_distinct_elements([1,2,1,2,1,2,1], 2) == 2
    assert max_distinct_elements([1,1,1,1,1,1,1], 2) == 1