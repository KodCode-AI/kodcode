from solution import *

def test_max_coprime_components():
    values = [2, 3, 6, 9, 10]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    assert max_coprime_components(values, edges) == 1

    values = [4, 6, 15, 35]
    edges = [[0, 1], [0, 2], [1, 3]]
    assert max_coprime_components(values, edges) == 2

    values = [2, 2, 2, 2]
    edges = [[0, 1], [0, 2], [0, 3]]
    assert max_coprime_components(values, edges) == -1

    values = [2, 3, 5]
    edges = [[0, 1], [0, 2]]
    assert max_coprime_components(values, edges) == -1

test_max_coprime_components()