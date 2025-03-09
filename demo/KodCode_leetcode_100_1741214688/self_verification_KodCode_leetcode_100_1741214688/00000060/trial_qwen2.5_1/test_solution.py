from solution import *

def test_min_task_time():
    assert min_task_time([2, 3, 5], 1) == 12
    assert min_task_time([2, 3, 5], 2) == 10
    assert min_task_time([1, 2, 3], 3) == 0
    assert min_task_time([], 0) == 0
    assert min_task_time([5], 0) == 5
    assert min_task_time([1, 2, 3, 4, 5], 2) == 14