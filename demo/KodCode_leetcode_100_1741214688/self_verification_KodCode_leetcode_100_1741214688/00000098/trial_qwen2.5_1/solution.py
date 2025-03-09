class CBTArrayInserter:
    def __init__(self, tree):
        self.tree = tree
        self.size = len(tree)

    def insert(self, target):
        self.size += 1
        index = self.size - 1
        self.tree.append(target)
        while index > 0 and self.tree[index] != 0:
            parent = (index - 1) // 2
            self.tree[parent] |= self.tree[index]
            index = parent
        return 0

    def get_root(self):
        return 0