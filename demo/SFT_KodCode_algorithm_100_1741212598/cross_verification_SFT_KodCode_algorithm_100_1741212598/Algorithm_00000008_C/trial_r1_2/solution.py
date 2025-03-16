class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

def detect_cycle(linked_list: LinkedList) -> bool:
    """Returns True if a cycle exists in the linked list using Floyd's cycle detection algorithm."""
    if linked_list.head is None:
        return False
    slow = linked_list.head
    fast = linked_list.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False