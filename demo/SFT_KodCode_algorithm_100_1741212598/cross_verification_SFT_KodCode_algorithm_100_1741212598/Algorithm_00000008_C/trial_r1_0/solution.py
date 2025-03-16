class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def detect_cycle(linked_list):
    if linked_list is None or linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False