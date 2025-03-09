from solution import *

def test_max_tasks():
    assert max_tasks([(2, 10), (1, 5), (1, 7), (1, 3)]) == [0, 2, 1]
    assert max_tasks([(1, 100), (2, 10)]) == [0]
    assert max_tasks([(1, 1), (1, 1), (1, 1)]) == [0, 1, 2]
    assert max_tasks([(4, 20), (1, 10), (1, 40), (1, 30)]) == [2, 0]
    assert max_tasks([(1, 5), (2, 10), (2, 15), (1, 20)]) == [2, 1, 0]