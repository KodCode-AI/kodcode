from solution import *

import pytest

def test_manhattan_distance_improved_positive_numbers():
    assert manhattan_distance_improved([1, 1], [2, 2]) == 2.0

def test_manhattan_distance_improved_mixed_dimensions():
    assert manhattan_distance_improved([1.5, 1.5], [2, 2]) == 1.0

def test_manhattan_distance_improved_mixed_dimensions_2():
    assert manhattan_distance_improved([1.5, 1.5], [2.5, 2]) == 1.5

def test_manhattan_distance_improved_large_dimensions():
    assert manhattan_distance_improved([0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1.0

def test_manhattan_distance_improved_input_validation():
    with pytest.raises(TypeError):
        manhattan_distance_improved([1, 1], None)

    with pytest.raises(ValueError):
        manhattan_distance_improved([1, 1], [2, 2, 2])

    with pytest.raises(TypeError):
        manhattan_distance_improved([1, "one"], [2, 2, 2])