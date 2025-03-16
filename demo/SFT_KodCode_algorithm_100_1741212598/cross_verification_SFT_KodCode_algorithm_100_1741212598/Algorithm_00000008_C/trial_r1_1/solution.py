class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def detect_cycle(linked_list: LinkedList) -> bool:
    if linked_list.head is None:
        return False
    
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head
    
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        
        if slow_ptr == fast_ptr:
            return True
    
    return False