class CustomQueue:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, value):
        if self.size == self.capacity:
            return False
        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def getQueue(self):
        current_list = []
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            current_list.append(self.array[index])
        return current_list