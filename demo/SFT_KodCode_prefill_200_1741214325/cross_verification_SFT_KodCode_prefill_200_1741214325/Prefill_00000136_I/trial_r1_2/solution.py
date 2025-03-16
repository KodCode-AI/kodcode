class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Cannot dequeue from an empty queue")
        return self.queue.pop(0)

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.queue)       # Output: [3]