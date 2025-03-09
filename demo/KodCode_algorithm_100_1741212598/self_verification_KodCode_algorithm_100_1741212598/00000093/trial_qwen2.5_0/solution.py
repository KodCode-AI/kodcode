from collections import defaultdict

class Node:
    def __init__(self, item, count=1):
        self.item = item
        self.count = count
        self.children = {}
        self.parent = None

    def add_child(self, child):
        if child.item not in self.children:
            self.children[child.item] = child
            child.parent = self

def construct_fp_tree(transactions, min_sup):
    item_freq = defaultdict(int)
    # Count item frequencies
    for transaction in transactions:
        for item in transaction:
            item_freq[item] += 1

    # Filter items by min_sup
    filtered_items = {item: freq for item, freq in item_freq.items() if freq >= min_sup}

    if not filtered_items:
        return None, {}

    head_table = {}
    for transaction in transactions:
        subset = [item for item in transaction if item in filtered_items]
        if subset:
            head_table = update_header_table(head_table, subset, filtered_items)

    # Construct FP-tree
    root = Node(None)
    for transaction in transactions:
        subset = [item for item in transaction if item in filtered_items]
        if subset:
            pre = root
            for item in subset:
                if not pre.children.get(item):
                    pre.children[item] = Node(item)
                pre = pre.children[item]
    return root, head_table

def update_header_table(head_table, transaction, item_freq):
    for item in transaction:
        if item in head_table:
            head_table[item][1] += item_freq[item]
        else:
            # Create a new entry
            head_table[item] = [None, item_freq[item], None]
    return head_table

# Example usage
def mine_frequent_itemsets(fp_tree, head_table, min_len=1):
    patterns = []
    def recurse_tree(node, prefix):
        if node.item:
            for next_node in node.children.values():
                new_prefix = prefix + [node.item]
                if len(new_prefix) >= min_len:
                    patterns.append(new_prefix)
                recurse_tree(next_node, new_prefix)
    
    if fp_tree is not None:
        recurse_tree(fp_tree, [])
    return patterns

# Example usage (full function)
def frequent_itemsets(transactions, min_sup):
    root, head_table = construct_fp_tree(transactions, min_sup)
    return mine_frequent_itemsets(root, head_table)