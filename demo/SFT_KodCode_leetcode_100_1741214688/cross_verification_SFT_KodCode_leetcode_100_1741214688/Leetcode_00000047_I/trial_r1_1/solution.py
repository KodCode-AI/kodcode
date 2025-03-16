from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            return None  # or raise an exception
        return self.q1.popleft()

    def top(self):
        if self.empty():
            return None  # or raise an exception
        return self.q1[0]

    def empty(self):
        return not self.q1