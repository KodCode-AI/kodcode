from heapq import heappush, heappop

class CustomPriorityQueue:
    def __init__(self):
        self.queue = {}  # Dictionary to hold the heap for each priority level

    def enqueue(self, priority, score):
        """
        Add a task to the queue with the given priority and score.
        """
        if priority not in self.queue:
            self.queue[priority] = []
        # Push the score and priority as a tuple (to support ordering by score, then priority)
        heappush(self.queue[priority], (-score, -priority, score))  # Using negative to simulate max-heap

    def dequeue(self):
        """
        Remove and return the task with the highest priority (and score if priorities are the same),
        following FIFO within each priority level.
        """
        while self.queue and not self.queue[self.queue[min(self.queue, key=lambda k: (min(self.queue[k], key=lambda x: x[0])[0], -k))]]:
            heappop(self.queue[min(self.queue, key=lambda k: (min(self.queue[k], key=lambda x: x[0])[0], -k))])
        if not self.queue:
            raise IndexError("dequeue from an empty queue")
        # Pop from the priority with the highest score (and highest priority if scores are equal)
        priority, score, _ = heappop(min(self.queue, key=lambda k: (min(self.queue[k], key=lambda x: x[0])[0], -k)))
        return score

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        result = {}
        for priority, pq in self.queue.items():
            result[priority] = [task[2] for task in pq]
        return str(result)

    def __len__(self):
        """
        Return the number of elements in the queue.
        """
        return sum(len(pq) for pq in self.queue.values())