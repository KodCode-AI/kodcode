class CBTArrayInserter:
    def __init__(self, tree):
        self.tree = tree
        self.n = len(tree)

    def insert(self, target):
        self.n += 1
        index = self.n - 1
        self.tree.append(target)
        while index > 0:
            parent = (index - 1) // 2
            if self.tree[index] == self.tree[parent] or self.tree[index] != self.tree[parent]:
                self.tree[parent] = self.tree[index] | self.tree[2 * parent + 1] | self.tree[2 * parent + 2]
            index = parent
        return 0

    def get_root(self):
        return self.n