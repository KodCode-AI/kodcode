from solution import *

import pytest

def test_circular_queue():
    circular_queue = CircularQueue(3)
    assert circular_queue.enQueue(1) == True
    assert circular_queue.enQueue(2) == True
    assert circular_queue.enQueue(3) == True
    assert circular_queue.Front() == 1
    assert circular_queue.deQueue() == True
    assert circular_queue.Rear() == 2
    assert circular_queue.enQueue(4) == True
    assert circular_queue.Front() == 2

    circular_queue2 = CircularQueue(2)
    assert circular_queue2.enQueue(1) == True
    assert circular_queue2.enQueue(2) == True
    assert circular_queue2.enQueue(3) == False  # Should return false as the queue is full
    assert circular_queue2.deQueue() == True
    assert circular_queue2.enQueue(3) == True
    assert circular_queue2.Rear() == 3

    circular_queue3 = CircularQueue(1)
    assert circular_queue3.enQueue(1) == True
    assert circular_queue3.deQueue() == True
    assert circular_queue3.isEmpty() == True
    assert circular_queue3.Front() == -1
    assert circular_queue3.deQueue() == False  # Should return false as the queue is empty