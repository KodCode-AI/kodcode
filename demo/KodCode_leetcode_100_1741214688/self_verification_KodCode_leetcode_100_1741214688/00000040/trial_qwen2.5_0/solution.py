class CustomQueue:
    def __init__(self, capacity: int):
        self.queue = []
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    def enqueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.append(value)
        self.rear += 1
        return True

    def dequeue(self) -> int:
        if self.isEmpty():
            return -1
        value = self.queue[self.front]
        self.front += 1
        return value

    def isFull(self) -> bool:
        return self.rear - self.front == self.capacity

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def getQueue(self) -> list:
        return self.queue[self.front:self.rear]