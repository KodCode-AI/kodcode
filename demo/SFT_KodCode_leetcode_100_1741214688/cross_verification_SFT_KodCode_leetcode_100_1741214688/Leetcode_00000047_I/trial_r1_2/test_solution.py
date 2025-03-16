from solution import *

import pytest
from solution import MyStack

def test_push_and_pop():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

def test_top():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.top() == 2  # did not pop, should still be 2
    assert stack.pop() == 2
    assert stack.top() == 1
    assert stack.pop() == 1
    assert stack.top() is None

def test_empty():
    stack = MyStack()
    assert stack.empty() == True
    stack.push(1)
    assert stack.empty() == False
    stack.pop()
    assert stack.empty() == True

def test_multiple_pushes():
    stack = MyStack()
    for i in range(5):
        stack.push(i)
    for i in range(4, -1, -1):
        assert stack.pop() == i
    assert stack.empty() == True