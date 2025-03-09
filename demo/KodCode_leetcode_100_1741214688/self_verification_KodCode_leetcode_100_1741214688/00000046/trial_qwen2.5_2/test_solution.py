from solution import *

def test_findLCA():
    node_values = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[4, 7], [3, 5]]
    expected = [2, 2]
    assert findLCA(queries, node_values) == expected

    node_values = [
        [1],
        [2, 3],
        [4, 5, 6, 7]
    ]
    queries = [[8, 9], [3, 4]]
    expected = [-1, -1]
    assert findLCA(queries, node_values) == expected

    node_values = [
        [1]
    ]
    queries = [[1, 1]]
    expected = [1]
    assert findLCA(queries, node_values) == expected

    node_values = [
        [1, 2],
        [3, None, 4, 5]
    ]
    queries = [[1, 5], [4, 3]]
    expected = [1, -1]
    assert findLCA(queries, node_values) == expected