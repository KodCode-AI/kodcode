from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Temporary queue

    def push(self, x: int) -> None:
        self.q1.append(x)
    
    def pop(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty")
        # Move all elements except the last to q2
        while len(self.q1) > 1:
            elem = self.q1.popleft()
            self.q2.append(elem)
        # Pop the last element from q1
        top = self.q1.popleft()
        # Swap q1 and q2 for future operations
        self.q1, self.q2 = self.q2, self.q1
        return top
    
    def top(self) -> int:
        if self.empty():
            raise IndexError("Stack is empty")
        # Move all elements except the last to q2
        while len(self.q1) > 1:
            elem = self.q1.popleft()
            self.q2.append(elem)
        # Get the top element
        top = self.q1[0]
        # Move the top element back to q2
        top_elem = self.q1.popleft()
        self.q2.append(top_elem)
        # Swap q1 and q2 for future operations
        self.q1, self.q2 = self.q2, self.q1
        return top
    
    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0