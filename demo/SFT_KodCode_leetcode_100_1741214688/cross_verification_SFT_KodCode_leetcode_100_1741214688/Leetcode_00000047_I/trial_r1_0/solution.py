from collections import deque

class MyStack:

    def __init__(self):
        self.currentq = deque()
        self.otherq = deque()

    def push(self, x):
        self.currentq.append(x)

    def pop(self):
        if self.empty():
            raise IndexError("pop from empty stack")
        while len(self.currentq) > 1:
            elem = self.currentq.popleft()
            self.otherq.append(elem)
        res = self.currentq.popleft()
        self.currentq, self.otherq = self.otherq, self.currentq
        return res

    def top(self):
        if self.empty():
            raise IndexError("top from empty stack")
        while len(self.currentq) > 1:
            elem = self.currentq.popleft()
            self.otherq.append(elem)
        top_elem = self.currentq[0]
        self.otherq.append(top_elem)
        self.currentq.popleft()
        self.currentq, self.otherq = self.otherq, self.currentq
        return top_elem

    def empty(self):
        return len(self.currentq) == 0 and len(self.otherq) == 0