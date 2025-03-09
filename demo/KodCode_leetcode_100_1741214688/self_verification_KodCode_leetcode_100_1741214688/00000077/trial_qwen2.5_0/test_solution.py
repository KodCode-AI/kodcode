from solution import *

import pytest
from solution import find_node_for_max_components

def test_empty_tree():
    assert find_node_for_max_components([], []) == -1

def test_single_node():
    assert find_node_for_max_components([1], []) == -1

def test_coprime_case1():
    values = [2, 3, 6, 9, 10]
    edges = [(0, 1), (1, 2), (1, 3), (3, 4)]
    assert find_node_for_max_components(values, edges) == 1

def test_non_coprime_case1():
    values = [4, 5, 6, 7, 8]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert find_node_for_max_components(values, edges) == 3

def test_no_optimal_node():
    values = [2, 4, 6, 8, 10]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert find_node_for_max_components(values, edges) == -1