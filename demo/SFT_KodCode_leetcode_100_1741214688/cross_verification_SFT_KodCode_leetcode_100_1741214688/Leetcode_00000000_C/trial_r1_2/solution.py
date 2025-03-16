class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.data = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def Front(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1) % self.k]

    def enQueue(self, value):
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.size -= 1
        self.front = (self.front + 1) % self.k
        return True

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k