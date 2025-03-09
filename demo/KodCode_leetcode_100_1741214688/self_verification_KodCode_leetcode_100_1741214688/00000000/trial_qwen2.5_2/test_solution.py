from solution import *

from circular_queue import CircularQueue

def test_circular_queue_ops():
    q = CircularQueue(3)
    assert q.enQueue(1) == True
    assert q.enQueue(2) == True
    assert q.enQueue(3) == True
    assert q.enQueue(4) == False
    assert q.Rear() == 3
    assert q.Front() == 1
    assert q.deQueue() == True
    assert q.enQueue(4) == True
    assert q.Front() == 2

def test_is_empty_and_is_full():
    q = CircularQueue(1)
    assert q.isFull() == False
    assert q.isEmpty() == True
    assert q.enQueue(1) == True
    assert q.isFull() == True
    assert q.isEmpty() == False
    assert q.deQueue() == True
    assert q.isFull() == False
    assert q.isEmpty() == True

def test_deQueue_empty_queue():
    q = CircularQueue(2)
    assert q.deQueue() == False