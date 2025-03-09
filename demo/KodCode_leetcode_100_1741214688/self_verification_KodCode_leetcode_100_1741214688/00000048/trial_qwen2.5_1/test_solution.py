from solution import *

def test_minCompletionTime():
    assert minCompletionTime([(1, 3, 2), (2, 5, 3), (7, 9, 1)]) == 10
    assert minCompletionTime([(0, 2, 1)]) == 3
    assert minCompletionTime([(1, 2, 1), (3, 4, 2)]) == 5
    assert minCompletionTime([(10, 12, 3), (11, 13, 2), (8, 10, 1)]) == 14
    assert minCompletionTime([]) == 0

test_minCompletionTime()