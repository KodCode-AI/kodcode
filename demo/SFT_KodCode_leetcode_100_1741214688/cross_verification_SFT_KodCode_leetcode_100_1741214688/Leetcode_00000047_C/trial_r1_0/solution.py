from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Auxiliary queue
    
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self) -> int:
        if self.empty():
            raise IndexError("pop from an empty stack")
        return self.q1.popleft()
    
    def top(self) -> int:
        if self.empty():
            raise IndexError("top from an empty stack")
        return self.q1[0]
    
    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0