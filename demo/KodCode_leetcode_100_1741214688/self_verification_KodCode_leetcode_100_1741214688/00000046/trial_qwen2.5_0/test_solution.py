from solution import *

from solution import build_tree_from_list, find_node, find_lca, lca_in_binary_tree

def test_tree_construction():
    tree_str = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[4, 7], [3, 5]]
    result = lca_in_binary_tree(tree_str, queries)
    assert result == [2, 2]

def test_no_node():
    tree_str = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[4, 8]]
    result = lca_in_binary_tree(tree_str, queries)
    assert result == [-1]

def test_root_lca():
    tree_str = [
        [1]
    ]
    queries = [[1, 1]]
    result = lca_in_binary_tree(tree_str, queries)
    assert result == [1]

def test_empty_queries():
    tree_str = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = []
    result = lca_in_binary_tree(tree_str, queries)
    assert result == []

def test_different_trees():
    tree_str1 = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries1 = [[4, 7], [3, 5]]
    result1 = lca_in_binary_tree(tree_str1, queries1)
    tree_str2 = [
        [1],
        [2, 3],
        [4, 5, 6]
    ]
    queries2 = [[4, 5], [3, 6]]
    result2 = lca_in_binary_tree(tree_str2, queries2)
    assert result1 == result2