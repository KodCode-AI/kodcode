from solution import *

import pytest

def test_flip_and_invert_image():
    assert flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
    assert flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

def test_single_row():
    assert flip_and_invert_image([[1]]) == [[0]]

def test_empty_matrix():
    assert flip_and_invert_image([]) == []

def test_all_zeros():
    assert flip_and_invert_image([[0,0,0],[0,0,0]]) == [[1,1,1],[1,1,1]]

def test_all_ones():
    assert flip_and_invert_image([[1,1,1],[1,1,1]]) == [[0,0,0],[0,0,0]]