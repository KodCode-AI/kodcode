from solution import *

def test_count_valid_triangles():
    assert count_valid_triangles([2, 2, 3, 4]) == 3
    assert count_valid_triangles([4, 2, 3]) == 1
    assert count_valid_triangles([3, 2, 3, 4]) == 5
    assert count_valid_triangles([5, 4, 3, 1, 2]) == 7
    assert count_valid_triangles([10, 21, 22, 100, 101, 200, 300]) == 0
    assert count_valid_triangles([1, 2, 3, 4, 5, 10]) == 10