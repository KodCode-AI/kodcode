from solution import *

from solution import can_win_game

def test_can_win_game_with_all_nonzero_blocks():
    assert can_win_game([1, 1, 1]) == True

def test_can_win_game_with_one_zero_block():
    assert can_win_game([0, 1, 1]) == False
    assert can_win_game([1, 0, 1]) == False
    assert can_win_game([1, 1, 0]) == False

def test_can_win_game_with_two_zero_blocks():
    assert can_win_game([0, 0, 1]) == False
    assert can_win_game([1, 0, 0]) == False

def test_can_win_game_with_zero_blocks():
    assert can_win_game([0, 0, 0]) == False