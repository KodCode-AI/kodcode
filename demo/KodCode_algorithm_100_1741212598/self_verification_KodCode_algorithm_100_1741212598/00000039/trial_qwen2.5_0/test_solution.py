from solution import *

import pytest
from solution import cube_root

def test_cube_root_positive_perfect_cubes():
    assert cube_root(27) == 3
    assert cube_root(64) == 4
    assert cube_root(125) == 5

def test_cube_root_negative_perfect_cubes():
    assert cube_root(-27) == -3
    assert cube_root(-64) == -4
    assert cube_root(-125) == -5

def test_cube_root_non_perfect_cubes():
    assert cube_root(28) is None
    assert cube_root(26) is None
    assert cube_root(80) is None

def test_cube_root_zero():
    assert cube_root(0) == 0

def test_cube_root_negative_zero():
    assert cube_root(-0) == 0

def test_cube_root_non_integer():
    with pytest.raises(TypeError):
        cube_root("a")
    with pytest.raises(TypeError):
        cube_root(3.5)

def test_large_numbers():
    assert cube_root(1000000000) == 100
    assert cube_root(-1000000000) == -100

def test_edge_cases():
    assert cube_root(1) == 1
    assert cube_root(-1) == -1
    assert cube_root(2) is None
    assert cube_root(-2) is None