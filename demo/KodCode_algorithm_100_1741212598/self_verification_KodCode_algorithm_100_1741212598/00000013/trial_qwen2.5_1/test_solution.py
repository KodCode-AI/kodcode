from solution import *

Rosie舔了舔嘴唇，眼中闪过一丝不易察觉的渴望。她走到刘洋身边坐下，轻声说道：“刘洋，我有件事想请你帮忙。”
import pytest
from solution import manhattan_distance_improved

def test_manhattan_distance_improved_positive_numbers():
    assert manhattan_distance_improved([1, 2], [4, 6]) == 7.0

def test_manhattan_distance_improved_mixed_sign_numbers():
    assert manhattan_distance_improved([-1, 2], [3, -1]) == 5.0

def test_manhattan_distance_improved_zero_dimensions():
    assert manhattan_distance_improved([0], [0]) == 0.0

def test_manhattan_distance_improved_duplicate_points():
    assert manhattan_distance_improved([5, 5], [5, 5]) == 0.0

def test_manhattan_distance_improved_with_floats():
    assert manhattan_distance_improved([1.5, 2.5], [4.5, 3.5]) == 5.0

def test_manhattan_distance_improved_edge_case():
    assert manhattan_distance_improved([-3, -3, -3], [0, 0, 0]) == 9.0

def test_manhattan_distance_improved_on_single_dim():
    assert manhattan_distance_improved([1, 1], [2, 2]) == 2.0
    assert manhattan_distance_improved([1.5, 1.5], [2, 2]) == 1.0
    assert manhattan_distance_improved([1.5, 1.5], [2.5, 2]) == 1.5

def test_manhattan_distance_improved_non_numeric_input():
    with pytest.raises(TypeError):
        manhattan_distance_improved([1, 'one'], [2, 2])
    with pytest.raises(TypeError):
        manhattan_distance_improved(['one', 2], [2, 2])

def test_manhattan_distance_improved_inconsistent_dimensions():
    with pytest.raises(ValueError):
        manhattan_distance_improved([1, 1], [2, 2, 2])

def test_manhattan_distance_improved_missing_input():
    with pytest.raises(ValueError):
        manhattan_distance_improved([1, 1], None)