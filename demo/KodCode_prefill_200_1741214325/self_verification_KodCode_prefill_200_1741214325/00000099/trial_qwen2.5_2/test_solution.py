from solution import *

from solution import detect_cycle, dfs_visit

def test_dfs_visit_no_cycle():
    graph = {
        0: [1],
        1: [2],
        2: []
    }
    assert not dfs_visit(graph, 0, set(), set())

def test_dfs_visit_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    assert dfs_visit(graph, 0, set(), set())

def test_detect_cycle_no_cycle():
    graph = {
        0: [1],
        1: [2],
        2: []
    }
    assert not detect_cycle(graph)

def test_detect_cycle_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    assert detect_cycle(graph)