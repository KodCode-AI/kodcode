from solution import *

import unittest

def load_data(filepath):
    """
    Loads transaction data from a file.
    :param filepath: Path to the file
    :return: List of itemsets
    """
    with open(filepath, 'r') as file:
        transactions = [set(map(int, line.strip().split())) for line in file]
    return transactions

class TestFPGrowth(unittest.TestCase):

    def setUp(self):
        self.transactions = load_data('transactions.txt')  # Assuming a file with transactions

    def test_create_fptree(self):
        min_sup = 2
        tree, filtered_items, header_table = create_fptree(self.transactions, min_sup)
        self.assertEqual(filtered_items, {1, 3, 4})
        self.assertIn(3, header_table)
        self.assertIn(4, header_table)
        self.assertIn(1, header_table.keys())

    def test_mine_frequent_itemsets(self):
        min_sup = 2
        min_len = 2
        min_sup_count = 3
        min_sup_item = 1
        expected_itemsets = [[1, 3], [1, 4], [1, 3, 4]]
        tree, _, header_table = create_fptree(self.transactions, min_sup)
        frequent_itemsets = mine_frequent_itemsets(tree, header_table, min_len, [])
        self.assertEqual(frequent_itemsets, expected_itemsets)

if __name__ == "__main__":
    unittest.main()