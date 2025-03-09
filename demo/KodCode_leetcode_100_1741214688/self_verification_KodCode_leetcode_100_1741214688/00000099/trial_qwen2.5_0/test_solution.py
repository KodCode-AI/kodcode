from solution import *

import pytest

def test_flip_and_invert_image():
    assert flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]) == [[1,0,0],[0,1,0],[1,1,1]]
    assert flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]) == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

def test_single_row_odd():
    assert flip_and_invert_image([[0]]) == [[1]]

def test_single_row_even():
    assert flip_and_invert_image([[1,0]]) == [[0,1]]

def test_zero_matrix():
    assert flip_and_invert_image([[0,0],[0,0]]) == [[1,1],[1,1]]

def test_mixed():
    assert flip_and_invert_image([[1,0,1],[0,1,0],[1,0,1]]) == [[0,1,0],[1,0,1],[0,1,0]]