from solution import *

import pytest

def test_cube_root_perfect_cubes():
    assert cube_root(27) == 3
    assert cube_root(64) == 4
    assert cube_root(125) == 5

def test_cube_root_non_perfect_cubes():
    assert cube_root(28) is None
    assert cube_root(35) is None
    assert cube_root(1) is None

def test_cube_root_negative_numbers():
    with pytest.raises(TypeError):
        cube_root(-27)

def test_cube_root_zero():
    assert cube_root(0) == 0

def test_cube_root_large_numbers():
    assert cube_root(27 ** 3) == 27
    assert cube_root((10**9) ** (1/3) ** 3) == 10**3

def test_cube_root_non_integers():
    with pytest.raises(TypeError):
        cube_root("27")

def test_cube_root_edge_cases():
    assert cube_root(8) == 2
    assert cube_root(1) is None