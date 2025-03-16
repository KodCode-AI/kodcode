from typing import List

class CustomQueue:
    """A class to implement a queue with fixed capacity."""
    
    def __init__(self, capacity: int):
        """Initialize the queue with the given capacity."""
        self.capacity = capacity
        self.queue = []
    
    def enqueue(self, value: int) -> bool:
        """Add a value to the end of the queue if there is space. Returns False if the queue is full."""
        if len(self.queue) >= self.capacity:
            return False
        self.queue.append(value)
        return True
    
    def dequeue(self) -> int:
        """Remove and return the value at the front of the queue. Returns -1 if the queue is empty."""
        if not self.queue:
            return -1
        return self.queue.pop(0)
    
    def isFull(self) -> bool:
        """Return True if the queue is full, otherwise False."""
        return len(self.queue) == self.capacity
    
    def isEmpty(self) -> bool:
        """Return True if the queue is empty, otherwise False."""
        return len(self.queue) == 0
    
    def getQueue(self) -> List[int]:
        """Return the current elements in the queue as a list, maintaining the order."""
        return self.queue.copy()