from solution import *

from solution import exist

def test_exist_positive_case():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "ABCCED") == True

def test_exist_with_visited_case():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "SEE") == True

def test_exist_multiple_path_case():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "ABCB") == False

def test_exist_different_board_shape():
    board = [
        ['A','B','C'],
        ['S','F','C'],
        ['A','D','E']
    ]
    assert exist(board, "ABFCACDB") == True

def test_exist_single_char_case():
    board = [["A"]]
    assert exist(board, "A") == True

def test_exist_word_not_found():
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert exist(board, "ABCG") == False

def test_exist_empty_board():
    board = []
    assert exist(board, "A") == False