from solution import *

from solution import find_lca_in_tree, TreeNode

def test_find_lca_in_tree():
    level_order = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[4, 7], [3, 5]]
    assert find_lca_in_tree(level_order, queries) == [2, 2]

    level_order = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[1, 3], [1, 5], [1, 7]]
    assert find_lca_in_tree(level_order, queries) == [1, 1, 1]

    level_order = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[4, 4], [5, 5]]
    assert find_lca_in_tree(level_order, queries) == [4, 5]

    level_order = [[1]]
    queries = [[1, 1]]
    assert find_lca_in_tree(level_order, queries) == [1]

    level_order = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[8, 9]]
    assert find_lca_in_tree(level_order, queries) == [-1]

test_find_lca_in_tree()