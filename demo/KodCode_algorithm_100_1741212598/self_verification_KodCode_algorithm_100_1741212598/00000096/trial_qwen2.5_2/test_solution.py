from solution import *

import pytest

def test_lfu_cache():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) is None
    cache.put(4, 4)
    assert cache.get(1) is None
    assert cache.get(3) == 3
    assert cache.get(4) == 4

def test_lfu_cache_with_duplicates():
    cache = LFUCache(1)
    cache.put(2, 1)
    assert cache.get(2) == 1
    cache.put(2, 2)
    assert cache.get(2) == 2
    cache.put(1, 1)
    assert cache.get(2) is None
    assert cache.get(1) == 1
    cache.put(4, 1)
    assert cache.get(1) is None
    assert cache.get(2) is None
    assert cache.get(3) is None
    assert cache.get(4) == 1

def test_lfu_cache_with_empty_cache():
    cache = LFUCache(0)
    assert cache.get(1) is None
    cache.put(1, 1)
    assert cache.get(1) is None

def test_lfu_cache_with_large_capacity():
    cache = LFUCache(1000)
    for i in range(1000):
        cache.put(i, i)
        assert cache.get(i) == i
    cache.put(1001, 1001)
    assert cache.get(0) is None
    assert cache.get(1000) is None
    assert cache.get(1001) == 1001