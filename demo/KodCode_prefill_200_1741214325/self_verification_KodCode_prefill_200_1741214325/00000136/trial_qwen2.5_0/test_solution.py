from solution import *

def test_queue_operations():
    q = Queue()
    assert q.is_empty() == True
    assert q.size() == 0

    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty() == True
    assert q.size() == 0

    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5
    assert q.is_empty() == True
    assert q.size() == 0

    try:
        q.dequeue()
        assert False, "Expected an IndexError but did not raise"
    except IndexError:
        assert True

    try:
        q.dequeue()
        assert False, "Expected an IndexError but did not raise"
    except IndexError:
        assert True

# The following tests are designed to ensure that enqueue and dequeue work with any type of item.
def test_enqueue_dequeue_with_different_types():
    q = Queue()
    q.enqueue(1)
    q.enqueue("2")
    assert q.dequeue() == 1
    assert q.dequeue() == "2"

    q.enqueue({"key": "value"})
    q.enqueue([1, 2, 3])
    assert q.dequeue() == {"key": "value"}
    assert q.dequeue() == [1, 2, 3]

    try:
        q.dequeue()
        assert False, "Expected an IndexError but did not raise"
    except IndexError:
        assert True

    try:
        q.dequeue()
        assert False, "Expected an IndexError but did not raise"
    except IndexError:
        assert True