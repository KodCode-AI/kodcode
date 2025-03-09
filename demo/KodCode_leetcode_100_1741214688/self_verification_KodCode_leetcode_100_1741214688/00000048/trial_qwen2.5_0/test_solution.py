from solution import *

def test_minCompletionTime():
    assert minCompletionTime([(1, 3, 2)]) == 3
    assert minCompletionTime([(1, 3, 2), (2, 5, 3), (7, 9, 1)]) == 10
    assert minCompletionTime([(1, 2, 1), (3, 4, 2), (5, 6, 1)]) == 6
    assert minCompletionTime([(1, 5, 3), (6, 8, 2), (10, 12, 4)]) == 12
    assert minCompletionTime([(0, 1, 1), (1, 3, 1), (3, 4, 1)]) == 4