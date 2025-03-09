from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Push the new element to q1
        self.q1.append(x)
        # Move all elements back from q2 to q1
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        if self.q1:  # If stack is not empty
            return self.q1.popleft()
        return None

    def top(self) -> int:
        if self.q1:  # If stack is not empty
            x = self.q1.popleft()
            self.push(x)  # Push it back to the stack
            return x
        return None

    def empty(self) -> bool:
        return not self.q1