from typing import List

class CBTArrayInserter:
    def __init__(self, tree: List[int]):
        self.tree = tree
        self.size = len(tree)
    
    def insert(self, target: int) -> int:
        self.size += 1
        index = self.size - 1
        self.tree.append(target)
        return 0
    
    def get_root(self) -> int:
        return 0