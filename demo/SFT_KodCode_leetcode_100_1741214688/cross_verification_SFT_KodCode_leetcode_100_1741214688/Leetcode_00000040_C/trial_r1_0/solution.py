class CustomQueue:
    def __init__(self, capacity):
        self.capacity = max(0, capacity)
        self.queue = []

    def enqueue(self, value):
        if len(self.queue) >= self.capacity:
            return False
        self.queue.append(value)
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.queue.pop(0)

    def isFull(self):
        return len(self.queue) == self.capacity

    def isEmpty(self):
        return len(self.queue) == 0

    def getQueue(self):
        return self.queue.copy()