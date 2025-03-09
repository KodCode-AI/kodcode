from solution import *

import pytest

def test_queue_empty():
    queue = Queue()
    assert queue.is_empty()
    assert queue.dequeue() is None

def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert not queue.is_empty()
    assert queue.queue == [1, 2]

def test_queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.queue == [1, 2, 3]

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.queue == [2, 3]

def test_queue_dequeue_empty():
    queue = Queue()
    assert queue.dequeue() is None

def test_queue_dequeue_multi_times():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()