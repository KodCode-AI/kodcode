from solution import *

from solution import exist

def test_exist_simple_word():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "ABCCED") == True

def test_exist_complex_word():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "SEE") == True

def test_exist_not_existing_word():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "ABCB") == False

def test_exist_single_char_word():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "A") == True

def test_exist_empty_word():
    assert exist([], "") == True

def test_exist_single_row_board():
    board = [
        ['A','B','C','E']
    ]
    assert exist(board, "ABCCED") == True

def test_exist_single_column_board():
    board = [
        ['A'],
        ['B'],
        ['C'],
        ['D'],
        ['E']
    ]
    assert exist(board, "ABCDE") == True

def test_exist_single_element_board():
    board = [
        ['A']
    ]
    assert exist(board, "A") == True

def test_exist_large_board():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
        ['S','F','C','S'],
        ['A','B','D','E']
    ]
    assert exist(board, "ABCB") == False