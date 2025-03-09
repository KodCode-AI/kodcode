from solution import *

from solution import min_time_to_complete_tasks

def test_min_time_to_complete_tasks_1():
    assert min_time_to_complete_tasks([1, 2, 3, 4, 5], 2) == 9
    assert min_time_to_complete_tasks([4, 2, 3, 2], 1) == 7

def test_min_time_to_complete_tasks_2():
    assert min_time_to_complete_tasks([1, 1, 1], 0) == 3
    assert min_time_to_complete_tasks([1], 1) == 1

def test_min_time_to_complete_tasks_3():
    assert min_time_to_complete_tasks([10, 10, 10, 10], 2) == 20
    assert min_time_to_complete_tasks([5, 5, 5, 5], 1) == 13

def test_min_time_to_complete_tasks_4():
    assert min_time_to_complete_tasks([1, 2, 3], 3) == 6
    assert min_time_to_complete_tasks([1], 0) == 1