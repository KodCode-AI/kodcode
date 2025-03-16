from solution import *

from solution import enqueue, dequeue

def test_enqueue_dequeue():
    queue = []
    enqueue(queue, 1)
    enqueue(queue, 2)
    assert dequeue(queue) == 1
    assert dequeue(queue) == 2
    assert dequeue(queue) is None

def test_enqueue():
    queue = []
    enqueue(queue, 1)
    assert queue == [1]
    enqueue(queue, 2)
    assert queue == [1, 2]

def test_dequeue_empty_queue():
    queue = []
    assert dequeue(queue) is None