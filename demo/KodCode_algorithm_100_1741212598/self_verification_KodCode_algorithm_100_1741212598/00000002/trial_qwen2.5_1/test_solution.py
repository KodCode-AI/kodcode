from solution import *

import pytest

def test_stack_with_queues():
    stack = StackWithQueues()
    stack.push(5)
    stack.push(4)
    stack.push(6)
    stack.push(3)

    # Test get_min
    assert stack.get_min() == 3

    # Test pop and get_min
    assert stack.pop() == 3
    assert stack.get_min() == 4

    # Test push and get_min
    stack.push(1)
    assert stack.push(1) == 1
    assert stack.get_min() == 1

    # Test push and get_min when all elements are equal
    stack.push(1)
    assert stack.get_min() == 1

    # Test pop multiple times and get_min
    assert stack.pop() == 1
    assert stack.pop() == 1
    assert stack.get_min() == 4
    assert stack.pop() == 6
    assert stack.get_min() == 4
    assert stack.pop() == 4
    assert stack.get_min() == 5
    with pytest.raises(IndexError):
        stack.pop()

    # Test get_min with an empty stack
    assert stack.get_min() is None