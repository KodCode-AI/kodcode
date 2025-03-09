import heapq

class CustomPriorityQueue:
    def __init__(self):
        self.priorities = [{}, {}, {}]  # Dicts to hold (score, task_id) for each priority

    def enqueue(self, priority, score):
        if priority not in range(3):
            raise ValueError("Priority must be between 0 and 2")
        task_id = len(self.priorities[priority])
        self.priorities[priority][score] = task_id

    def dequeue(self):
        for priority in range(2, -1, -1):
            if self.priorities[priority]:
                keys = list(self.priorities[priority].keys())
                score = min(keys)
                task_id = self.priorities[priority].pop(score)
                return score
        return None

    def __repr__(self):
        priorities_repr = []
        for i, priority_dict in enumerate(self.priorities):
            if priority_dict:
                min_score = min(priority_dict.keys())
                tasks = list(priority_dict.keys())
                tasks.remove(min_score)
                tasks.insert(0, min_score)
                priorities_repr.append(f"Priority {i}: [{', '.join(map(str, tasks))}]")
        return ', '.join(priorities_repr)