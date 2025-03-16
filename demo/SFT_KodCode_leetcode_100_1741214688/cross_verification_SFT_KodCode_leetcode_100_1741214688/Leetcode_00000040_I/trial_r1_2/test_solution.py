from solution import *

import pytest

def test_customqueue_operations():
    custom_queue = CustomQueue(3)
    assert custom_queue.enqueue(1) is True
    assert custom_queue.enqueue(2) is True
    assert custom_queue.enqueue(3) is True
    assert custom_queue.enqueue(4) is False  # Queue is full
    assert custom_queue.dequeue() == 1
    assert custom_queue.getQueue() == [2, 3]
    assert custom_queue.dequeue() == 2
    assert custom_queue.dequeue() == 3
    assert custom_queue.dequeue() == -1  # Queue is empty
    assert custom_queue.enqueue(5) is True
    assert custom_queue.getQueue() == [5]

def test_queue_limit():
    custom_queue = CustomQueue(2)
    assert custom_queue.enqueue(1) is True
    assert custom_queue.enqueue(2) is True
    assert custom_queue.isFull() is True
    assert custom_queue.enqueue(3) is False
    assert custom_queue.getQueue() == [1, 2]

def test_empty_queue():
    custom_queue = CustomQueue(2)
    assert custom_queue.isEmpty() is True
    assert custom_queue.enqueue(1) is True
    assert custom_queue.getQueue() == [1]
    assert custom_queue.isEmpty() is False
    assert custom_queue.dequeue() == 1
    assert custom_queue.isEmpty() is True

def test_enqueue_and_dequeue_mixed():
    custom_queue = CustomQueue(2)
    assert custom_queue.enqueue(1) is True
    assert custom_queue.enqueue(2) is True
    assert custom_queue.dequeue() == 1
    assert custom_queue.enqueue(3) is True
    assert custom_queue.getQueue() == [2, 3]
    assert custom_queue.dequeue() == 2
    assert custom_queue.dequeue() == 3
    assert custom_queue.isEmpty() is True