from solution import *

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

def test_init():
    cache = LFUCache(0)
    assert cache.capacity == 0
    assert cache.node_dict == {}
    assert cache.freq_map == defaultdict(DoubleLinkedList)
    assert cache.min_freq == 0

def test_put():
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.node_dict == {1: Node(1, 1, 2), 3: Node(3, 3, 1)}
    assert cache.min_freq == 1
    cache.put(4, 4)
    assert cache.node_dict == {3: Node(3, 3, 2), 4: Node(4, 4, 1)}  # 1 is evicted
    assert cache.min_freq == 1

def test_get():
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