from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x: int) -> None:
        self.q1.append(x)
    
    def pop(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty")
        # Ensure q1 has the most recent elements
        if len(self.q1) == 0:
            self.q1, self.q2 = self.q2, self.q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()
        # Swap queues for future operations
        self.q1, self.q2 = self.q2, self.q1
        return popped
    
    def top(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty")
        # Ensure q1 has the most recent elements
        if len(self.q1) == 0:
            self.q1, self.q2 = self.q2, self.q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        return self.q1[-1]
    
    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0