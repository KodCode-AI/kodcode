from solution import *

from typing import List

def test_min_intervals_to_remove():
    assert min_intervals_to_remove([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert min_intervals_to_remove([[1,2],[1,2],[1,2]]) == 2
    assert min_intervals_to_remove([[1,2],[2,3]]) == 0
    assert min_intervals_to_remove([[5,10],[10,15],[15,20]]) == 0
    assert min_intervals_to_remove([[1,5],[1,5],[1,5]]) == 2
    assert min_intervals_to_remove([[1,2],[2,3],[2,4],[3,5],[4,6],[4,7]]) == 2
    assert min_intervals_to_remove([[0,30],[5,10],[15,20]]) == 1
    assert min_intervals_to_remove([[1,10],[2,21],[3,22],[4,30]]) == 3