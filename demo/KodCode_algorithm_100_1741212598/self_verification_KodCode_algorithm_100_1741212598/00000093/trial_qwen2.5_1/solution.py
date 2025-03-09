from collections import defaultdict

def create_fptree(transactions, min_sup):
    """
    Constructs an FP-tree from the given transactions.
    :param transactions: List of itemsets (transaction items are sets)
    :param min_sup: Minimum support threshold
    :return: FP-Tree, items below min_sup, header table
    """
    # Count frequencies of each item
    freq_items = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            freq_items[item] += 1

    # Filter items by min_sup
    filtered_items = {item for item, count in freq_items.items() if count >= min_sup}
    freq_items = {item: count for item, count in freq_items.items() if item in filtered_items}

    # Initialize FP-Tree
    root = {}

    # Populate FP-Tree
    for transaction in transactions:
        reduced_transaction = {item for item in transaction if item in filtered_items}
        if reduced_transaction:
            add_to_tree(root, reduced_transaction, freq_items)

    # Build header table
    header_table = add_to_header_table(filtered_items, freq_items)

    return root, filtered_items, header_table

def add_to_tree(tree, transaction, freq_items):
    """
    Adds transaction to the tree.
    :param tree: Current tree node
    :param transaction: Ordered transaction
    :param freq_items: Frequency of each item
    :return: None
    """
    current = tree
    for item in transaction:
        if item not in current:
            current[item] = {}
        current = current[item]

def add_to_header_table(items, freq_items):
    """
    Adds items to header table.
    :param items: Dictionary of items and their frequencies
    :return: Header table
    """
    header_table = defaultdict(list)
    for item, count in items.items():
        header_table[count].append(item)
    return dict(sorted(header_table.items(), reverse=True))

def mine_frequent_itemsets(tree, header_table, min_len, prefix_path):
    """
    Mines frequent itemsets from the FP-tree.
    :param tree: FP-Tree
    :param header_table: Header table
    :param min_len: Minimum length of itemset
    :param prefix_path: Prefix path for current itemset
    :return: List of frequent itemsets
    """
    frequent_itemsets = []
    for item, items in header_table.items():
        for item_path in items:
            new_path = prefix_path + [item]
            if len(new_path) >= min_len:
                frequent_itemsets.append(new_path)
            # Conditional FP-tree for sub-path
            cond_tree, cond_header = conditional_pattern_base(tree, item)
            if cond_header:
                conditional_frequent_itemsets = mine_frequent_itemsets(cond_tree, cond_header, min_len, new_path)
                frequent_itemsets.extend(conditional_frequent_itemsets)
    return frequent_itemsets

def conditional_pattern_base(tree, item):
    """
    Extracts conditional pattern base.
    :param tree: Tree node
    :param item: Target item
    :return: Conditional tree, header table
    """
    prefix_path = []
    while tree[item] is not None:
        path = trace_path(tree, item)
        prefix_path.append([item] + path)
        tree = tree[item]
    return build_conditional_tree(prefix_path, item), build_header_table(prefix_path, item)

def trace_path(tree, item):
    """
    Traces path from tree to root for an item.
    :param tree: Tree node
    :param item: Target item
    :return: Path from item to root
    """
    path = []
    while item is not None:
        path.append(item)
        item = next(iter(tree[item].keys()), None)
    return path[1:]

def build_conditional_tree(prefix_path, item):
    """
    Builds conditional tree.
    :param prefix_path: Prefix path
    :param item: Target item
    :return: Conditional tree
    """
    conditional_tree = {}
    for transaction in prefix_path:
        reduced_transaction = [i for i in transaction if i != item]
        if reduced_transaction:
            add_to_tree(conditional_tree, reduced_transaction, None)
    return conditional_tree

def build_header_table(prefix_path, item):
    """
    Builds header table for conditional tree.
    :param prefix_path: Prefix path
    :param item: Target item
    :return: Header table
    """
    header_table = defaultdict(list)
    for transaction in prefix_path:
        for i in transaction:
            if i != item:
                header_table[i].append(transaction)
    return header_table