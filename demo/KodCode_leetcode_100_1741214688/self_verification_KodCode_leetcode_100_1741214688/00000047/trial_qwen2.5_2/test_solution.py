from solution import *

def test_my_stack():
    stack = MyStack()

    # Test push
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2  # top() should return 2
    assert stack.pop() == 2  # pop() should return 2

    # Test multiple operations
    stack.push(3)
    assert stack.top() == 3  # top() should return 3
    assert stack.pop() == 3  # pop() should return 3
    assert stack.pop() == 1  # pop() should return 1

    # Test empty stack
    assert stack.empty() == True  # empty() should return True

    # Test after all operations
    stack.push(4)
    assert stack.top() == 4  # top() should return 4
    assert stack.pop() == 4  # pop() should return 4
    assert stack.empty() == True  # empty() should return True

    # Test empty stack again
    stack.push(5)
    assert stack.top() == 5  # top() should return 5
    assert stack.pop() == 5  # pop() should return 5
    assert stack.empty() == True  # empty() should return True

    # Test pop from empty stack
    stack.push(6)
    assert stack.top() == 6  # top() should return 6
    assert stack.pop() == 6  # pop() should return 6
    try:
        stack.pop()  # This should raise an error
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError for pop from an empty stack"

    try:
        stack.top()  # This should raise an error
    except IndexError:
        pass
    else:
        assert False, "Expected IndexError for top from an empty stack"