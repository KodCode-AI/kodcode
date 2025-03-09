from solution import *

from solution import flip_and_invert_image

def test_flip_and_invert_image():
    grid = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    expected = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    assert flip_and_invert_image(grid) == expected

def test_flip_and_invert_image_single_row():
    grid = [[1, 1, 1]]
    expected = [[0, 0, 0]]
    assert flip_and_invert_image(grid) == expected

def test_flip_and_invert_image_all_zeros():
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    expected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert flip_and_invert_image(grid) == expected

def test_flip_and_invert_image_all_ones():
    grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert flip_and_invert_image(grid) == expected

def test_flip_and_invert_image_mixed():
    grid = [[1, 0, 1], [1, 1, 0], [0, 0, 0]]
    expected = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    assert flip_and_invert_image(grid) == expected