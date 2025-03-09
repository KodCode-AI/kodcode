from solution import *

import pytest
from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    # Implementation as provided in the solution
    left, right = 0, len(lst) - 1
    
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < lst[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return lst[left] if left < len(lst) and lst[left] >= lst[(left - 1) % len(lst)] else None

def test_find_peak_positive():
    assert find_peak([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5
    assert find_peak([1, 10, 9, 8, 7, 6, 5, 4]) == 10
    assert find_peak([1, 9, 8, 7]) == 9
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 0]) == 7
    assert find_peak([1, 2, 3, 4, 3, 2, 1, 0, -1, -2]) == 4
    assert find_peak([1, 2, 2, 1, 0, -1, -2]) == 2
    assert find_peak([1, 1]) == 1
    assert find_peak([1]) == 1
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10]) == 12
    assert find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11, 10, 9]) == 12

def test_find_peak_negative():
    assert find_peak([1, 3, 3, 2, 0]) is None
    assert find_peak([1, 3, 3, 3, 2, 0]) is None
    assert find_peak([1, 3, 2, 0]) is None
    assert find_peak([1, 3, 2, 1, 0]) is None