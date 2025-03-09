from solution import *

from custom_priority_queue import CustomPriorityQueue

def test_custom_priority_queue():
    cq = CustomPriorityQueue()
    cq.enqueue(0, 10)
    cq.enqueue(1, 15)
    cq.enqueue(2, 20)
    cq.enqueue(0, 12)
    cq.enqueue(1, 14)
    cq.enqueue(2, 22)
    assert str(cq) == "{'0': [10, 12], '1': [15, 14], '2': [20, 22]}"
    assert cq.dequeue() == 10
    assert str(cq) == "{'0': [12], '1': [15, 14], '2': [20, 22]}"
    assert cq.dequeue() == 12
    assert str(cq) == "{'1': [15, 14], '2': [20, 22]}"
    assert cq.dequeue() == 15