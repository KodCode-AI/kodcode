class Queue:
    """
    A basic queue implementation using a list.
    Methods:
        enqueue(item): Adds an item to the end of the queue.
        dequeue(): Removes and returns the item from the front of the queue.
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("pop from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)