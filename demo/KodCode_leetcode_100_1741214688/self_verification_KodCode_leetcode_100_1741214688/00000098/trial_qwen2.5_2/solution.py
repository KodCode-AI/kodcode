class CBTArrayInserter:
    def __init__(self, tree):
        self.tree = tree
        self.size = len(tree)

    def insert(self, target):
        self.size += 1
        index = self.size - 1
        self.tree.append(target)
        while index > 0:
            parent = (index - 1) // 2
            if self.tree[parent] != self.tree[index] | self.tree[parent]:
                self.tree[parent] |= self.tree[index]
                index = parent
            else:
                break
        return 0

    def get_root(self):
        return 0