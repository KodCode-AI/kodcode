class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
    try:
        print(q.dequeue())
    except IndexError as e:
        print(e)  # Output: Cannot dequeue from an empty queue.