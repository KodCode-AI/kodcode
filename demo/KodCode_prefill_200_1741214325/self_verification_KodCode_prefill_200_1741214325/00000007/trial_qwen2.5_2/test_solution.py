from solution import *

from solution import can_win_greedy_game

def test_can_win_greedy_game_all_blocks():
    assert can_win_greedy_game(1, 1, 1) == True

def test_can_win_greedy_game_two_blocks():
    assert can_win_greedy_game(1, 0, 1) == True
    assert can_win_greedy_game(0, 1, 1) == True
    assert can_win_greedy_game(1, 1, 0) == True

def test_cannot_win_greedy_game_less_than_three_blocks():
    assert can_win_greedy_game(0, 0, 0) == False
    assert can_win_greedy_game(1, 0, 0) == False
    assert can_win_greedy_game(0, 1, 0) == False
    assert can_win_greedy_game(0, 0, 1) == False

def test_cannot_win_greedy_game_no_common_blocks():
    assert can_win_greedy_game(0, 0, 0) == False
    assert can_win_greedy_game(0, 0, 1) == False
    assert can_win_greedy_game(0, 1, 0) == False
    assert can_win_greedy_game(1, 0, 0) == False

def test_can_win_greedy_game_single_block():
    assert can_win_greedy_game(1, 0, 0) == True
    assert can_win_greedy_game(0, 1, 0) == True
    assert can_win_greedy_game(0, 0, 1) == True