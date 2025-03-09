class StackWithQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.min_value = None
    
    def push(self, item):
        """
        Pushes an item onto the stack.
        """
        if not self.queue1:
            self.queue1.append(item)
            self.min_value = item
        else:
            self.queue1.append(item)
            if item <= self.min_value:
                self.queue2.append(self.min_value)
                self.min_value = item
    
    def pop(self):
        """
        Removes and returns the top element from the stack.
        """
        if not self.queue1:
            raise IndexError("pop from an empty stack")
        if self.queue1[-1] == self.min_value:
            self.queue2.pop()
            self.min_value = self.queue2[-1] if self.queue2 else float('inf')
        return self.queue1.pop()
    
    def peek(self):
        """
        Returns the top element of the stack without removing it.
        """
        if not self.queue1:
            return None
        return self.queue1[-1]
    
    def get_min(self):
        """
        Returns the minimum element in the stack in O(1) time complexity.
        """
        return self.min_value