from solution import *

import pytest

def test_custom_priority_queue():
    cq = CustomPriorityQueue()
    cq.enqueue(0, 10)
    cq.enqueue(1, 15)
    cq.enqueue(2, 20)
    cq.enqueue(0, 12)
    cq.enqueue(1, 14)
    cq.enqueue(2, 22)
    assert repr(cq) == "Priority 0: [10, 12], Priority 1: [15, 14], Priority 2: [20, 22]"
    assert cq.dequeue() == 10
    assert repr(cq) == "Priority 0: [12], Priority 1: [15, 14], Priority 2: [20, 22]"
    assert cq.dequeue() == 12
    assert repr(cq) == "Priority 0: [], Priority 1: [15, 14], Priority 2: [20, 22]"
    assert cq.dequeue() == 15
    assert repr(cq) == "Priority 0: [], Priority 1: [14], Priority 2: [20, 22]"
    assert cq.dequeue() == 14
    assert repr(cq) == "Priority 0: [], Priority 1: [], Priority 2: [20, 22]"
    assert cq.dequeue() == 20
    assert repr(cq) == "Priority 0: [], Priority 1: [], Priority 2: [22]"
    assert cq.dequeue() == 22
    assert repr(cq) == "Priority 0: [], Priority 1: [], Priority 2: []"
    with pytest.raises(ValueError):
        cq.enqueue(3, 10)

test_custom_priority_queue()