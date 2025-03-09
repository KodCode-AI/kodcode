from typing import Generic, TypeVar, Dict, Optional

T = TypeVar('T')
U = TypeVar('U')

class Node:
    def __init__(self, key: T, value: U, freq: int):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None, None, 0)
        self.tail = Node(None, None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node: Node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop(self, node: Node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def head_node(self) -> Node:
        return self.head.next

class LFUCache(Generic[T, U]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.freq_map: Dict[int, DoubleLinkedList] = {}
        self.key_map: Dict[T, Node] = {}

    def get(self, key: T) -> U | None:
        if key not in self.key_map:
            return None
        node = self.key_map[key]
        self.increase_freq(node)
        return node.value

    def put(self, key: T, value: U) -> None:
        if self.capacity == 0:
            return
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.increase_freq(node)
        else:
            if self.size == self.capacity:
                lru_list = self.freq_map[self.min_freq]
                node_to_evict = lru_list.pop(lru_list.head_node())
                del self.key_map[node_to_evict.key]
                self.size -= 1
            new_node = Node(key, value, 1)
            self.key_map[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DoubleLinkedList()
            self.freq_map[1].append(new_node)
            self.min_freq = 1
            self.size += 1

    def increase_freq(self, node: Node):
        old_list = self.freq_map[node.freq]
        old_list.pop(node)
        if old_list.size == 0 and node.freq == self.min_freq:
            self.min_freq += 1
        node.freq += 1
        new_list = self.freq_map.setdefault(node.freq, DoubleLinkedList())
        new_list.append(node)