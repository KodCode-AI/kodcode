from heapq import heappush, heappop

class CustomPriorityQueue:
    def __init__(self):
        self._heap = []
        # This dictionary will keep track of tasks per priority level
        self._priorities = {priority: [] for priority in range(3)}

    def enqueue(self, priority, score):
        heappush(self._heap, (score, priority))
        self._priorities[priority].append(score)
        
    def dequeue(self):
        # Get the task with the highest priority
        score, priority = heappop(self._heap)
        # Ensure the list of tasks at the current priority is updated
        self._priorities[priority].remove(score)
        if not self._priorities[priority]:
            del self._priorities[priority]
        return score

    def __str__(self):
        return str({priority: tasks for priority, tasks in self._priorities.items()})