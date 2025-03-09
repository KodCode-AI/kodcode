from typing import List

def max_tasks(tasks: List[tuple[int, int]]) -> List[int]:
    """
    Returns the list of task indices that should be selected to achieve the maximum reward.
    """
    # Sort tasks based on their deadline in ascending order.
    tasks.sort(key=lambda x: x[0])
    
    selected_tasks = []
    tasks_to_select = []
    max_time = 0
    
    for deadline, reward in tasks:
        # If the current task can be completed within the max_time, add it to the selection.
        while max_time < deadline and tasks_to_select:
            selected_tasks.append(tasks_to_select.pop(-1)[1])
            max_time += 1

        # Add the current task to the selection if it and the next can be completed.
        if len(tasks_to_select) == 0 or tasks_to_select[-1][1] > reward:
            tasks_to_select.append((deadline, reward))
            tasks_to_select = sorted(tasks_to_select, key=lambda x: x[1], reverse=True)
            max_time = max(max_time, deadline)

    # Add the last selected task if it has a valid deadline.
    if tasks_to_select:
        selected_tasks.append(tasks_to_select.pop(-1)[1])

    # Sort the selected tasks to return them in the order of their original indices.
    return sorted([tasks.index(task[1]) for task in [(0, idx) for idx in selected_tasks]])