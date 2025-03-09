from solution import *

from solution import count_triangles

def test_count_triangles():
    assert count_triangles([2, 1, 3]) == 1
    assert count_triangles([5, 8, 6, 10, 7, 12]) == 8
    assert count_triangles([19, 18, 1, 7, 4, 15, 2, 12, 6, 10, 11, 14, 5, 16, 8, 13, 3, 9, 0]) == 33
    assert count_triangles([1, 2, 3, 4, 5]) == 6
    assert count_triangles([5, 5, 5, 5]) == 10
    assert count_triangles([10, 21, 22, 100, 101, 102]) == 4