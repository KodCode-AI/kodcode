from solution import *

import pytest
from solution import generate_gray_code

def test_generate_gray_code_with_edge_cases():
    with pytest.raises(ValueError):
        generate_gray_code(0)
    with pytest.raises(ValueError):
        generate_gray_code(-1)
    with pytest.raises(ValueError):
        generate_gray_code(3.5)

def test_generate_gray_code_with_small_values():
    assert generate_gray_code(1) == [0, 1]
    assert generate_gray_code(2) == [0, 1, 3, 2]
    assert generate_gray_code(3) == [0, 1, 3, 2, 6, 7, 5, 4]

def testGenerateGrayCodeWithLargerValues():
    assert generate_gray_code(4) == [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
    assert generate_gray_code(5) == [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 16, 17, 19, 18, 22, 23, 21, 20, 14, 15, 13, 12, 8, 9, 7, 6]

def testGenerateGrayCodeWithLargeValue():
    assert generate_gray_code(8) == [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, 48, 49, 51, 50, 54, 55, 53, 52, 44, 45, 47, 46, 42, 43, 41, 40, 32, 33, 35, 34, 38, 39, 37, 36]