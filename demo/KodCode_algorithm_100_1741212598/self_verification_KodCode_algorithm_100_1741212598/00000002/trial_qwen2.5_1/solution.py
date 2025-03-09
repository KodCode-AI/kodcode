from collections import deque

class StackWithQueues:
    def __init__(self):
        self.main_queue = deque()
        self.min_queue = deque()
        self._push_count = 0

    def push(self, item):
        """
        Pushes an integer item onto the stack.
        """
        self.main_queue.append(item)
        if self._push_count == 0 or item <= self.min_queue[-1]:
            self.min_queue.append(item)
        self._push_count += 1

    def pop(self):
        """
        Removes the top element from the stack and returns it. If the stack is empty, it should raise an IndexError.
        """
        if not self.main_queue:
            raise IndexError("pop from an empty stack")

        item = self.main_queue.popleft()
        if item == self.min_queue[-1]:
            self.min_queue.popleft()
        return item

    def peek(self):
        """
        Returns the top element of the stack without removing it. If the stack is empty, it should return None.
        """
        if not self.main_queue:
            return None
        return self.main_queue[0]

    def get_min(self):
        """
        Returns the minimum element in the stack in O(1) time complexity.
        """
        if not self.min_queue:
            return None
        return self.min_queue[-1]