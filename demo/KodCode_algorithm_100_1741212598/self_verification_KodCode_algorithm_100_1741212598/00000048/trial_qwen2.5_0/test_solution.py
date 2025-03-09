from solution import *

import heapq
from typing import List

def max_tasks(tasks: List[tuple[int, int]]) -> List[int]:
    tasks.sort(key=lambda x: x[0])  # Sort tasks by their deadline
    max_heap = []
    current_time = 0  # Represents the current time to schedule tasks
    task_indices = []  # Stores the indices of selected tasks

    for i, (deadline, reward) in enumerate(tasks):
        while max_heap and current_time < deadline - 1:
            _, task_index = heapq.heappop(max_heap)
            task_indices.remove(task_index)  # Remove from the list if it's not used in current window
            current_time += 1
        if deadline > current_time:
            heapq.heappush(max_heap, (-reward, i))  # Use negative value for max-heap behavior
            task_indices.append(i)
            current_time = deadline
        else:
            # If deadline is met, we use the most rewarding task available within the time
            if -max_heap[0][0] > reward:
                _, old_task_index = heapq.heappop(max_heap)
                task_indices.remove(old_task_index)  # Remove old task from indices
                task_indices.append(i)  # Add new task to indices
                heapq.heappush(max_heap, (-reward, i))  # Push new task

    return task_indices

def test_max_tasks():
    assert max_tasks([(2, 10), (1, 5), (1, 7), (1, 9)]) == [2, 0]
    assert max_tasks([(1, 2), (2, 4), (3, 8), (1, 10)]) == [3, 2]
    assert max_tasks([(2, 1)]) == [0]
    assert max_tasks([(2, 2), (2, 1), (1, 1)]) == [0]
    assert max_tasks([(1, 1), (1, 1), (1, 1)]) == [0, 1, 2]
    assert max_tasks([]) == []
    assert max_tasks([(1, 100), (1, 15)]) == [0]
    print("All tests passed!")

test_max_tasks()