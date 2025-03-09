from solution import *

from solution import num_paths_memo

def test_num_paths_memo():
    assert num_paths_memo(2, 3) == 3
    assert num_paths_memo(3, 2) == 3
    assert num_paths_memo(3, 3) == 6
    assert num_paths_memo(1, 1) == 1
    assert num_paths_memo(3, 7) == 28
    assert num_paths_memo(5, 5) == 70