from solution import *

import pytest

def test_max_tasks():
    # Test with tasks that have overlapping deadlines but different rewards
    tasks = [(4, 20), (1, 10), (1, 40), (1, 30)]
    assert max_tasks(tasks) == [2, 0]

    # Test with tasks where all deadlines are the same
    tasks = [(1, 100), (1, 100), (1, 200)]
    assert max_tasks(tasks) == [2]

    # Test with tasks where one task is invalid
    tasks = [(1, 10), (2, 20), (1, 100)]
    assert max_tasks(tasks) == [2]

    # Test with a single task
    tasks = [(1, 100)]
    assert max_tasks(tasks) == [0]

    # Test with an empty list
    tasks = []
    assert max_tasks(tasks) == []

    # Test with tasks where one task deadline is in the middle of the others
    tasks = [(2, 30), (1, 10), (3, 50)]
    assert max_tasks(tasks) == [2, 0]

    # Test with tasks where no task can be completed within its deadline
    tasks = [(2, 10), (1, 20)]
    assert max_tasks(tasks) == []

    # Test with tasks where all deadlines are the same but there is a mix of high and low rewards
    tasks = [(1, 50), (1, 30), (1, 100), (1, 20)]
    assert max_tasks(tasks) == [2]

# Run the tests
test_max_tasks()