from solution import *

import pytest

def test_can_win_game():
    assert can_win_game([1, 1, 1]) == False
    assert can_win_game([0, 2, 2]) == True
    assert can_win_game([1, 2, 3]) == True
    assert can_win_game([2, 1, 1]) == False
    assert can_win_game([3, 3, 3]) == True

def test_can_win_game_with_zeroes():
    assert can_win_game([0, 0, 0]) == False
    assert can_win_game([0, 1, 1]) == True
    assert can_win_game([1, 0, 1]) == True
    assert can_win_game([1, 1, 0]) == True

def test_can_win_game_with_large_numbers():
    assert can_win_game([5, 7, 9]) == True
    assert can_win_game([10, 10, 10]) == True
    assert can_win_game([20, 15, 10]) == True
    assert can_win_game([50, 50, 50]) == True