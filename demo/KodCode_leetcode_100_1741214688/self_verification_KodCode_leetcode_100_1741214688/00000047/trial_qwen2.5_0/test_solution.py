from solution import *

from collections import deque
import pytest

def test_my_stack():
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)
    assert my_stack.top() == 2
    assert my_stack.pop() == 2
    assert my_stack.empty() is False

    my_stack.push(3)
    assert my_stack.pop() == 3
    assert my_stack.pop() == 1
    assert my_stack.empty() is True