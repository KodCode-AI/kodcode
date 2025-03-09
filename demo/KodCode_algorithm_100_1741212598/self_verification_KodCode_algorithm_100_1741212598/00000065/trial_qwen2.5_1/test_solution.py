from solution import *

from solution import optimized_odd_even_transposition

def test_optimized_odd_even_transposition():
    assert optimized_odd_even_transposition([4, 1, 3, 2]) == [1, 2, 3, 4]
    assert optimized_odd_even_transposition([-5, 9, -2, 10, -1]) == [-5, -2, -1, 9, 10]
    assert optimized_odd_even_transposition([100]) == [100]
    assert optimized_odd_even_transposition([]) == []
    assert optimized_odd_even_transposition([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert optimized_odd_even_transposition([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]
    assert optimized_odd_even_transposition([1, 2, 2, 1]) == [1, 1, 2, 2]