from solution import *

def test_two_sum_indices():
    assert two_sum_indices([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_indices([2, 7, 11, 15], 17) == [0, 3]
    assert two_sum_indices([2, 7, 11, 15], 18) == [1, 2]
    assert two_sum_indices([2, 7, 11, 15], 26) == [2, 3]
    assert two_sum_indices([1, 3, 3], 6) == [1, 2]
    assert two_sum_indices([2, 7, 11, 15], 8) == []
    assert two_sum_indices([3 * i for i in range(10)], 19) == []
    assert two_sum_indices([1, 2, 3], 6) == []
    print("All tests passed!")

if __name__ == "__main__":
    test_two_sum_indices()