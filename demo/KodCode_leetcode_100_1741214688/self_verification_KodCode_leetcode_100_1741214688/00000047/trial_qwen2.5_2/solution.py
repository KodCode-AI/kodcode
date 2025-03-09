from collections import deque

class MyStack:
    """
    Implements a stack using two queues.
    """
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def push(self, x: int) -> None:
        """
        Pushes element x to the top of the stack.
        """
        # Always enqueue to queue2
        self.queue2.append(x)
        # Swap the queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Removes the element from the top of the stack and returns it.
        """
        # Ensure queue1 has at least one element
        if self.empty():
            raise IndexError("pop from an empty stack")
        # Pop from queue1 which now represents the top of the stack.
        return self.queue1.popleft()

    def top(self) -> int:
        """
        Returns the element at the top of the stack.
        """
        if self.empty():
            raise IndexError("top from an empty stack")
        # Return the first element of queue1 which is the top of the stack.
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.
        """
        return not self.queue1