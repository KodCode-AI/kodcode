from solution import *

import pytest

def test_optimized_partition():
    assert optimized_partition(1) == 1
    assert optimized_partition(9) == 14
    assert optimized_partition(1000000) == 55374
    assert optimized_partition(500000) == 373354
    assert optimized_partition(200000) == 107943

def test_partition_function():
    partition = [0] * 101
    partition[0] = 1
    for i in range(1, 101):
        for k in range(i, 101):
            partition[k] += partition[k - i]
    assert partition[100] % 1000000 == 0
    assert partition.index(0, 100) == 55374