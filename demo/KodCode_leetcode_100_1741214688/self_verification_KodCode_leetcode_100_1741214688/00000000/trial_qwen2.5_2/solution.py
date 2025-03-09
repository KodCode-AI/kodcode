class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class CircularQueue:
    def __init__(self, k):
        self.max_size = k
        self.size = 0
        self.head = None
        self.tail = None

    def Front(self):
        return -1 if self.head is None else self.head.value

    def Rear(self):
        return -1 if self.head is None else self.tail.value

    def enQueue(self, value):
        if self.size == self.max_size:
            return False
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1
        return True

    def deQueue(self):
        if self.head is None:
            return False
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return True

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return self.size == self.max_size