class CircularQueue:
    def __init__(self, k: int):
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.current_size = 0
        self.queue = [-1] * k

    def Front(self) -> int:
        return self.queue[self.front] if self.current_size else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.current_size else -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.current_size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.max_size
        self.current_size -= 1
        if self.current_size == 0:
            self.rear = -1
        return True

    def isEmpty(self) -> bool:
        return self.current_size == 0

    def isFull(self) -> bool:
        return self.current_size == self.max_size