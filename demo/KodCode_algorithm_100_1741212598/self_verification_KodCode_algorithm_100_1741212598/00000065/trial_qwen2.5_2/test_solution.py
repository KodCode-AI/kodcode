from solution import *

import pytest
from solution import optimized_odd_even_transposition

def test_optimized_odd_even_transposition():
    assert optimized_odd_even_transposition([4, 1, 3, 2]) == [1, 2, 3, 4]
    assert optimized_odd_even_transposition([-5, 9, -2, 10, -1]) == [-5, -2, -1, 9, 10]
    assert optimized_odd_even_transposition([7, 2, 9, 5, 4, 3, 1]) == [1, 2, 3, 4, 5, 7, 9]
    assert optimized_odd_even_transposition([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]
    assert optimized_odd_even_transposition([]) == []
    assert optimized_odd_even_transposition([5]) == [5]
    assert optimized_odd_even_transposition([-10, -20, -30, -40, -50]) == [-50, -40, -30, -20, -10]

def test_performance():
    # Test performance on a large dataset
    large_dataset = list(range(100000))
    import time
    start_time = time.time()
    optimized_odd_even_transposition(large_dataset)
    end_time = time.time()
    assert (end_time - start_time) < 10  # Assuming it should complete in less than 10 seconds

    large_dataset.reverse()
    start_time = time.time()
    optimized_odd_even_transposition(large_dataset)
    end_time = time.time()
    assert (end_time - start_time) < 10  # Similarly for a reverse sorted list

def test_duplicates():
    assert optimized_odd_even_transposition([4, 1, 3, 2, 2, 3, 4]) == [1, 2, 2, 3, 3, 4, 4]
    assert optimized_odd_even_transposition([-5, 9, -2, 10, -1, -2, 9]) == [-5, -2, -2, -1, 9, 9, 10]