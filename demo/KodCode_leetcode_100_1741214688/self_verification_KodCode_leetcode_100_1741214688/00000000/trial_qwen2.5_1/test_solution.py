from solution import *

import pytest

def test_circular_queue():
    cq = CircularQueue(3)

    assert cq.enQueue(1) is True
    assert cq.enQueue(2) is True
    assert cq.enQueue(3) is True
    assert cq.enQueue(4) is False

    assert cq.Rear() == 3
    assert cq.Front() == 1

    assert cq.deQueue() is True
    assert cq.enQueue(4) is True

    assert cq.Front() == 2

def test_queue_operations():
    cq = CircularQueue(2)

    assert cq.enQueue(1) is True
    assert cq.enQueue(2) is True
    assert cq.enQueue(3) is False

    assert cq.deQueue() is True
    assert cq.enQueue(3) is True

    assert cq.Front() == 2
    assert cq.Rear() == 3

    assert cq.deQueue() is True
    assert cq.deQueue() is True
    assert cq.Rear() == -1
    assert cq.Front() == -1