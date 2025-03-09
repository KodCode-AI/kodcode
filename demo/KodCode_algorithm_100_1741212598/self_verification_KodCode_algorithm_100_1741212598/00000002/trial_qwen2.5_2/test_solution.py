from solution import *

import pytest

def test_stack_with_queues():
    stack = StackWithQueues()
    stack.push(5)
    stack.push(4)
    stack.push(6)
    stack.push(3)
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == 4
    stack.pop()
    assert stack.get_min() == 5
    stack.push(1)
    assert stack.get_min() == 1

def test_stack_pop_empty():
    stack = StackWithQueues()
    with pytest.raises(IndexError):
        stack.pop()

def test_stack_peek_empty():
    stack = StackWithQueues()
    assert stack.peek() is None

def test_stack_peek_non_empty():
    stack = StackWithQueues()
    stack.push(10)
    assert stack.peek() == 10
    stack.push(5)
    assert stack.peek() == 5

def test_stack_push_pop_sequence():
    stack = StackWithQueues()
    stack.push(4)
    stack.push(1)
    stack.push(5)
    assert stack.get_min() == 1
    assert stack.pop() == 5
    assert stack.pop() == 1
    assert stack.pop() == 4