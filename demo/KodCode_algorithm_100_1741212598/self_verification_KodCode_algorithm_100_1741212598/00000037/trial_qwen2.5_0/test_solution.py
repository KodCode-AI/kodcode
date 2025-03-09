from solution import *

import pytest

def test_optimized_partition():
    # Test with smaller values of n to verify the correctness
    assert optimized_partition(1) == 1
    assert optimized_partition(9) == 14

    # Test with a large value of n
    assert optimized_partition(1000000) == 55374

def test_partitions_zero():
    # Test the zero case
    assert optimized_partition(0) == 1

def test_partitions_divisibility():
    # Test divisibility for intermediate values
    assert optimized_partition(999999) != 0  # Should not be divisible by 1000000
    assert optimized_partition(55373) != 0  # Should not be divisible by 1000000
    assert optimized_partition(55374) == 0  # Should be divisible by 1000000