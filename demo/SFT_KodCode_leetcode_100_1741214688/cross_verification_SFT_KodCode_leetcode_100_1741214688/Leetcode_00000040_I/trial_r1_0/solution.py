class CustomQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity = capacity
        self.data = [0] * capacity
        self.front = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value):
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1
        value = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def getQueue(self):
        result = []
        current = self.front
        for _ in range(self.size):
            result.append(self.data[current])
            current = (current + 1) % self.capacity
        return result