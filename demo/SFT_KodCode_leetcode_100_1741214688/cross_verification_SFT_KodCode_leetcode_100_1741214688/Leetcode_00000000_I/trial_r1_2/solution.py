class CircularQueue:
    def __init__(self, k):
        self.k = k
        if self.k <= 0:
            self.data = []
            self.front = 0
            self.rear = 0
            self.count = 0
        else:
            self.data = [None] * self.k
            self.front = 0
            self.rear = 0
            self.count = 0

    def Front(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        index = (self.rear - 1) % self.k
        return self.data[index]

    def enQueue(self, value):
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.count -= 1
        self.front = (self.front + 1) % self.k
        return True

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.k