from typing import List

def max_tasks(tasks: List[tuple[int, int]]) -> List[int]:
    """
    Returns a list of task indices that yield the maximum reward given the deadlines.
    """
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