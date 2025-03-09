from solution import *

from solution import count_good_triangles

def test_count_good_triangles():
    assert count_good_triangles([2, 1, 3]) == 1
    assert count_good_triangles([5, 8, 6, 1, 4]) == 2
    assert count_good_triangles([1, 1, 1, 1]) == 0
    assert count_good_triangles([10, 20, 30]) == 0
    assert count_good_triangles([1, 2, 2, 3, 4]) == 3

def test_modulo_large():
    assert count_good_triangles([10, 0, 8, 6, 14, 12, 16, 18, 20, 22, 24, 26]) == 22