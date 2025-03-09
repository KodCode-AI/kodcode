from typing import Generic, TypeVar, Optional
import collections

T = TypeVar('T')
U = TypeVar('U')

class Node:
    def __init__(self, key: T, value: U, freq: int = 0):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_least_frequent(self):
        last_node = self.tail.prev
        self.remove(last_node)
        return last_node

    def __len__(self):
        return self.size

class LFUCache(Generic[T, U]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_linked_list = collections.defaultdict(DoubleLinkedList)
        self.min_freq = 0

    def get(self, key: T) -> U | None:
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self._increase_freq(node)
        return node.value

    def put(self, key: T, value: U) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._increase_freq(node)
        else:
            if len(self.key_to_node) == self.capacity:
                removed_node = self.freq_to_linked_list[self.min_freq].remove_least_frequent()
                del self.key_to_node[removed_node.key]
            new_node = Node(key, value, freq=1)
            self.key_to_node[key] = new_node
            self.freq_to_linked_list[1].add_to_head(new_node)
            self.min_freq = 1

    def _increase_freq(self, node: Node):
        old_freq = node.freq
        self.freq_to_linked_list[old_freq].remove(node)
        if old_freq == self.min_freq and not self.freq_to_linked_list[old_freq]:
            self.min_freq += 1
        node.freq += 1
        self.freq_to_linked_list[node.freq].add_to_head(node)