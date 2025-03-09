from collections import defaultdict

def create_header_table(transactions, min_sup):
    """
    Create a header table for frequent items.
    """
    item_freq = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_freq[item] += 1
    header_table = {item: (item_freq[item], None) for item in item_freq if item_freq[item] >= min_sup}
    return header_table

def create_fp_tree(transactions, header_table):
    """
    Create an FP-tree from the transactions and header table.
    """
    def remove_items(transaction, header_table):
        return [item for item in transaction if header_table.get(item) is not None]

    root = {}
    for transaction in transactions:
        transaction = remove_items(transaction, header_table)
        if transaction:
            add_to_tree(root, transaction)

    return root

def add_to_tree(tree, transaction):
    """
    Add a transaction to the tree.
    """
    if not transaction:
        return
    current = tree
    for item in transaction:
        if item not in current:
            current[item] = {}
        current = current[item]

def mine_frequent_itemsets(fp_tree, header_table, min_sup, prefix=[]):
    """
    Recursively mine the FP-tree to find all frequent itemsets.
    """
    def scan_db(node, prefix, min_sup, freq_items):
        if node is None:
            return
        for item, next in node.items():
            freq = node[item][0]
            if freq >= min_sup:
                freq_items[item] = freq
                prefix_copy = prefix + [item]
                print("Frequent itemset found: {} with support {}".format(prefix_copy, freq))
                scan_db(next, prefix_copy, min_sup, freq_items)
            scan_db(next, prefix, min_sup, freq_items)

    freq_items = defaultdict(int)
    scan_db(fp_tree, prefix, min_sup, freq_items)
    return freq_items

def fp_growth(transactions, min_sup):
    """
    Implementation of the FP-Growth algorithm.
    """
    header_table = create_header_table(transactions, min_sup)
    if not header_table:
        return []
    fp_tree = create_fp_tree(transactions, header_table)
    return mine_frequent_itemsets(fp_tree, header_table, min_sup)