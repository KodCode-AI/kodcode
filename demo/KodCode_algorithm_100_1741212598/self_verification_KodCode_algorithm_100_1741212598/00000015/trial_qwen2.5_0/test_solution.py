from solution import *

def test_custom_priority_queue():
    cq = CustomPriorityQueue()
    cq.enqueue(0, 10)
    cq.enqueue(1, 15)
    cq.enqueue(2, 20)
    cq.enqueue(0, 12)
    cq.enqueue(1, 14)
    cq.enqueue(2, 22)
    assert str(cq) == '{0: [10, 12], 1: [15, 14], 2: [20, 22]}'
    assert cq.dequeue() == 10
    assert str(cq) == '{0: [12], 1: [15, 14], 2: [20, 22]}'
    assert cq.dequeue() == 12
    assert str(cq) == '{0: [], 1: [15, 14], 2: [20, 22]}'
    assert cq.dequeue() == 15

def test_multiple_queues():
    cq = CustomPriorityQueue()
    cq.enqueue(0, 1)
    cq.enqueue(0, 2)
    cq.enqueue(1, 1)
    cq.enqueue(1, 2)
    assert str(cq) == '{0: [1, 2], 1: [1, 2]}'
    assert cq.dequeue() == 1
    assert str(cq) == '{0: [2], 1: [1, 2]}'
    assert cq.dequeue() == 2
    assert str(cq) == '{0: [], 1: [1, 2]}'
    assert cq.dequeue() == 1
    assert str(cq) == '{0: [], 1: [2]}'
    assert cq.dequeue() == 2

def test_empty_queue():
    cq = CustomPriorityQueue()
    assert cq.dequeue() is None