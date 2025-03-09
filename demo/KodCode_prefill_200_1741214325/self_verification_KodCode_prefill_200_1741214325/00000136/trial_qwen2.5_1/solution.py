class Queue:
    """
    Queue implementation using a list with enqueue and dequeue methods.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """
        Adds an element to the end of the queue.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes the element from the front of the queue. Returns None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.queue) == 0