class StackWithQueues:
    def __init__(self):
        self.main_queue = []
        self.min_queue = []

    def push(self, item):
        self.main_queue.append(item)
        if not self.min_queue or item <= self.min_queue[-1]:
            self.min_queue.append(item)

    def pop(self):
        if not self.main_queue:
            raise IndexError("pop from an empty stack")
        if self.main_queue[-1] == self.min_queue[-1]:
            self.min_queue.pop()
        return self.main_queue.pop()

    def peek(self):
        if not self.main_queue:
            return None
        return self.main_queue[-1]

    def get_min(self):
        if not self.min_queue:
            raise IndexError("get_min from an empty stack")
        return self.min_queue[-1]