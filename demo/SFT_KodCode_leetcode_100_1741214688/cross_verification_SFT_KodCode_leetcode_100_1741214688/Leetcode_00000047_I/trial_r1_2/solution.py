from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue holding the stack elements
        self.q2 = deque()  # Temporary queue for reversing order during push

    def push(self, x):
        # Add the new element to q2
        self.q2.append(x)
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap the queues: q1 now becomes q2, and q2 becomes empty
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
        return len(self.q1) == 0