from solution import *

def test_minCompletionTime():
    assert minCompletionTime([(1, 3, 2), (2, 5, 3), (7, 9, 1)]) == 10
    assert minCompletionTime([(1, 2, 1), (3, 5, 2), (4, 6, 2)]) == 7
    assert minCompletionTime([(1, 5, 1), (2, 3, 2)]) == 6
    assert minCompletionTime([(1, 2, 4), (3, 5, 3), (6, 8, 5)]) == 13
    assert minCompletionTime([(1, 10, 1), (2, 20, 2), (3, 30, 3)]) == 62

test_minCompletionTime()