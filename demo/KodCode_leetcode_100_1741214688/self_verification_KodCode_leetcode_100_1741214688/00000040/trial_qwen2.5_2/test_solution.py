from solution import *

import pytest

def test_custom_queue():
    q = CustomQueue(3)
    assert q.enqueue(1) == True
    assert q.enqueue(2) == True
    assert q.enqueue(3) == True
    assert q.enqueue(4) == False  # Queue is full
    assert q.isFull() == True
    assert q.isEmpty() == False
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.isFull() == False
    assert q.isEmpty() == False
    assert q.enqueue(4) == True
    assert q.enqueue(5) == True
    assert q.enqueue(6) == False  # Queue is full
    assert q.getQueue() == [4, 5]

def test_empty_queue():
    q = CustomQueue(1)
    assert q.enqueue(1) == True
    assert q.isEmpty() == False
    assert q.dequeue() == 1
    assert q.isEmpty() == True
    assert q.isFull() == False

def test_dequeue_empty():
    q = CustomQueue(3)
    assert q.dequeue() == -1

def test_get_queue():
    q = CustomQueue(5)
    assert q.getQueue() == []
    q.enqueue(1)
    q.enqueue(2)
    assert q.getQueue() == [1, 2]