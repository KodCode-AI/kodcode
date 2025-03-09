class CircularQueue:
    def __init__(self, k: int):
        assert k > 0, "k must be a positive integer"
        self.max_size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def Front(self) -> int:
        if self.head == -1:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.head == -1:
            return -1
        return self.queue[self.tail]

    def enQueue(self, value: int) -> bool:
        if self.head == -1 and self.tail == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = value
            return True
        elif (self.tail + 1) % self.max_size == self.head:
            return False
        else:
            self.tail = (self.tail + 1) % self.max_size
            self.queue[self.tail] = value
            return True

    def deQueue(self) -> bool:
        if self.head == -1:
            return False
        elif self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        else:
            self.head = (self.head + 1) % self.max_size
            return True

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.max_size == self.head