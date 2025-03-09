from typing import List

def max_tasks(tasks: List[tuple[int, int]]) -> List[int]:
    """
    Returns a list of task indices that yield the maximum reward based on their deadlines.
    Assumes task indices are 0-based.
    """
    # Sort tasks by their deadline in ascending order. If deadlines are the same, sort by reward in descending order.
    tasks.sort(key=lambda x: (x[0], -x[1]))
    
    selected_tasks = []
    for deadline, reward in tasks:
        # Find the first position where a task with this deadline or later can be inserted.
        pos = 0
        while pos < len(selected_tasks) and selected_tasks[pos] < deadline:
            pos += 1
        
        # If there's a valid position to insert the current task, do so.
        if pos < len(selected_tasks):
            selected_tasks[pos] = deadline
        else:
            # If no position is available, meaning we have the first deadline which can start immediately,
            # then we add it to the beginning of the list.
            if not selected_tasks or deadline >= selected_tasks[0]:
                selected_tasks.insert(0, deadline)
            else:
                # The current task cannot be added without violating the deadline constraint, so we skip it.
                continue
    
    # Extract the indices of the selected tasks.
    return [i for i, task in enumerate(tasks) if task[0] in selected_tasks]