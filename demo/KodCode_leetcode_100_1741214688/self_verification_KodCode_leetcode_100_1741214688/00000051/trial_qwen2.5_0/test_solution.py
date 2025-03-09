from solution import *

from pytest import mark, raises

@mark.unit
def test_custom_comparator():
    # Test with even length array
    arr = [4, 3, 1, 2]
    comparator = CustomComparator(arr)
    comparator.sort()
    assert comparator.getResult() == [1, 3, 2, 4]

    # Test with odd length array
    arr = [4, 3, 1]
    comparator = CustomComparator(arr)
    comparator.sort()
    assert comparator.getResult() == [1, 3, 4]

    # Test with array of length 2
    arr = [2, 1]
    comparator = CustomComparator(arr)
    comparator.sort()
    assert comparator.getResult() == [1, 2]

    # Test with reversed sorted array
    arr = [4, 2, 3, 1]
    comparator = CustomComparator(arr)
    comparator.sort()
    assert comparator.getResult() == [2, 4, 3, 1]