from solution import *

import pytest

def test_cube_root_perfect_cubes():
    assert cube_root(27) == 3
    assert cube_root(64) == 4
    assert cube_root(125) == 5
    assert cube_root(216) == 6
    assert cube_root(343) == 7
    assert cube_root(729) == 9

def test_cube_root_not_a_perfect_cube():
    assert cube_root(28) is None
    assert cube_root(29) is None
    assert cube_root(30) is None
    assert cube_root(31) is None
    assert cube_root(80) is None

def test_empty_input():
    assert cube_root(0) is None

def test_negative_input():
    assert cube_root(-27) is None

def test_large_input():
    assert cube_root(1000000000) == 1000

def test_invalid_input_type():
    with pytest.raises(TypeError):
        cube_root("a")
    with pytest.raises(TypeError):
        cube_root(1.5)