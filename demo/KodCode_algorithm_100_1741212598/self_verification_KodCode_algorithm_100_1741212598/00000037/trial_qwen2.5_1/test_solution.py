from solution import *

import pytest

def test_optimized_partition():
    assert optimized_partition(1) == 1
    assert optimized_partition(9) == 14
    assert optimized_partition(1000000) == 55374

def test_partition_k():
    assert partition_k(4, 2) == 5  # 4 = 2 + 2, 4 = 1 + 1 + 2, 4 = 2 + 1 + 1, 4 = 1 + 2 + 1, 4 = 1 + 1 + 1 + 1

def partition_k(n: int, k: int) -> int:
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return partition_k(n - k, k) + partition_k(n - 1, k - 1)

# If you want to disable the lru_cache during the tests
partition_k.cache_clear()