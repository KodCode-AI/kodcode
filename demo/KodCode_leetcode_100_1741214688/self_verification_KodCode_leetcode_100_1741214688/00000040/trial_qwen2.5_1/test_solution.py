from solution import *

import pytest

def test_custom_queue():
    max_size = 5
    custom_queue = CustomQueue(max_size)

    assert custom_queue.isEmpty() == True
    assert custom_queue.isFull() == False
    
    assert custom_queue.enqueue(10) == True
    assert custom_queue.enqueue(20) == True
    assert custom_queue.enqueue(30) == True
    assert custom_queue.enqueue(40) == True
    assert custom_queue.enqueue(50) == True
    assert custom_queue.enqueue(60) == False  # Queue is full

    assert custom_queue.isFull() == True
    assert custom_queue.isEmpty() == False

    assert custom_queue.getQueue() == [10, 20, 30, 40, 50]

    assert custom_queue.dequeue() == 10
    assert custom_queue.getQueue() == [20, 30, 40, 50, None]  # Note: The last None represent the tail pointer advancing

    assert custom_queue.enqueue(70) == True

    assert custom_queue.getQueue() == [20, 30, 40, 50, 70]

    assert custom_queue.dequeue() == 20
    assert custom_queue.dequeue() == 30
    assert custom_queue.getQueue() == [40, 50, 70, None, None]

    assert custom_queue.enqueue(80) == True
    assert custom_queue.enqueue(90) == True
    assert custom_queue.enqueue(100) == True
    assert custom_queue.enqueue(110) == False  # Queue is already full

    assert custom_queue.getQueue() == [40, 50, 70, 80, 90]

    assert custom_queue.dequeue() == 40
    assert custom_queue.dequeue() == 50
    assert custom_queue.dequeue() == 70
    assert custom_queue.dequeue() == 80
    assert custom_queue.dequeue() == 90
    assert custom_queue.getQueue() == [100, None, None, None, None]

    assert custom_queue.enqueue(120) == True
    assert custom_queue.dequeue() == 100
    assert custom_queue.dequeue() == 120
    assert custom_queue.dequeue() == -1  # Queue is now empty

    assert custom_queue.isEmpty() == True