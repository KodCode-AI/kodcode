from solution import *

``
import pytest

@pytest.fixture
def stack():
    return StackWithQueues()

def test_push_and_get_min(stack):
    stack.push(5)
    stack.push(4)
    stack.push(6)
    stack.push(3)
    assert stack.get_min() == 3

def test_pop_and_get_min(stack):
    stack.push(5)
    stack.push(4)
    stack.push(6)
    stack.push(3)
    stack.pop()
    assert stack.get_min() == 4

def test_push_equal_min(stack):
    stack.push(5)
    stack.push(5)
    assert stack.get_min() == 5

def test_pop_multiple_times(stack):
    stack.push(5)
    stack.push(3)
    stack.pop()
    stack.pop()
    with pytest.raises(IndexError):
        stack.get_min()

def test_empty_stack_get_min(stack):
    with pytest.raises(IndexError):
        stack.get_min()

def test_peek(stack):
    stack.push(5)
    assert stack.peek() == 5
    stack.pop()
    assert stack.peek() is None