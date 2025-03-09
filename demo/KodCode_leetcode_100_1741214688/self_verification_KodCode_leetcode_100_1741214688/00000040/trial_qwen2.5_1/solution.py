class CustomQueue:
    def __init__(self, capacity: int):
        assert capacity > 0, "Capacity must be greater than 0"
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, value: int) -> bool:
        if self.size < self.capacity:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1
            return True
        return False

    def dequeue(self) -> int:
        if self.size == 0:
            return -1
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def isFull(self) -> bool:
        return self.size == self.capacity

    def isEmpty(self) -> bool:
        return self.size == 0

    def getQueue(self) -> list:
        if self.head < self.tail:
            return self.queue[self.head:self.tail]
        else:
            return self.queue[self.head:] + self.queue[:self.tail]