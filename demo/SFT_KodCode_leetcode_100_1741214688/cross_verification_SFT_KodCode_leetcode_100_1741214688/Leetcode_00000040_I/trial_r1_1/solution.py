class CustomQueue:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.elements = [None] * self.max_capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, value):
        if self.size == self.max_capacity:
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % self.max_capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return -1
        value = self.elements[self.front]
        self.front = (self.front + 1) % self.max_capacity
        self.size -= 1
        return value

    def isFull(self):
        return self.size == self.max_capacity

    def isEmpty(self):
        return self.size == 0

    def getQueue(self):
        current = []
        index = self.front
        for _ in range(self.size):
            current.append(self.elements[index])
            index = (index + 1) % self.max_capacity
        return current