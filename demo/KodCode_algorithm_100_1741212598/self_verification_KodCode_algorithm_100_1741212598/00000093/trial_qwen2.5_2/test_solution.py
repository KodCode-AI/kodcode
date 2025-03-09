from solution import *

``
from solution import fp_growth

def test_create_header_table():
    transactions = [
        ['a', 'b', 'c'],
        ['a', 'b', 'x'],
        ['c', 'd', 'x'],
    ]
    header_table = create_header_table(transactions, 2)
    assert header_table == {'a': (2, None), 'b': (2, None), 'c': (2, None), 'x': (2, None)}

def test_create_fp_tree():
    header_table = {'a': (2, None), 'b': (2, None), 'c': (2, None), 'x': (2, None)}
    transactions = [
        ['a', 'b', 'c'],
        ['a', 'b', 'x'],
        ['c', 'd', 'x'],
    ]
    fp_tree = create_fp_tree(transactions, header_table)
    assert fp_tree == {'a': {'b': {'c': {}}, 'x': {}}, 'b': {}, 'c': {}, 'x': {}}

def test_mine_frequent_itemsets():
    transactions = [
        ['a', 'b', 'c'],
        ['a', 'b', 'x'],
        ['c', 'd', 'x'],
    ]
    header_table = create_header_table(transactions, 2)
    fp_tree = create_fp_tree(transactions, header_table)
    freq_items = mine_frequent_itemsets(fp_tree, header_table, 2)
    assert freq_items == {'a': 2, 'b': 2, 'c': 2, 'x': 2}

def test_fp_growth():
    transactions = [
        ['a', 'b', 'c'],
        ['a', 'b', 'x'],
        ['c', 'd', 'x'],
    ]
    min_sup = 2
    frequent_itemsets = fp_growth(transactions, min_sup)
    assert frequent_itemsets == {'a': 2, 'b': 2, 'c': 2, 'x': 2}

# To run tests, use: pytest -v <filename>.py