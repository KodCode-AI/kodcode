from collections import defaultdict
from typing import Dict, Any

class Node:
    def __init__(self, key: int, value: int, freq: int = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node: Node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_left(self) -> Node:
        if self.head.next == self.tail:
            return None
        node = self.head.next
        self.remove(node)
        return node

class LFUCache(Generic[int, int]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_dict: Dict[int, Node] = {}
        self.freq_map: Dict[int, DoubleLinkedList] = defaultdict(DoubleLinkedList)
        self.min_freq = 0

    def get(self, key: int) -> int | None:
        if key not in self.node_dict:
            return None
        node = self.node_dict[key]
        self.freq_map[node.freq].remove(node)
        if self.min_freq == node.freq and not self.freq_map[node.freq].size:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.node_dict:
            node = self.node_dict[key]
            node.value = value
            self.get(key)
            return
        if len(self.node_dict) == self.capacity:
            node_to_evict = self.freq_map[self.min_freq].pop_left()
            del self.node_dict[node_to_evict.key]
        new_node = Node(key, value)
        self.node_dict[key] = new_node
        self.freq_map[1].append(new_node)
        self.min_freq = 1