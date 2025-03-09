from solution import *

import pytest

def test_evaluate_expression():
    assert evaluate_expression("3+2*2") == 7
    assert evaluate_expression(" 3/2 ") == 1
    assert evaluate_expression(" 3+5 / 2 ") == 5
    assert evaluate_expression("1 + 2 * 3 / 4 - 5") == -2
    assert evaluate_expression("(2+6)* 4 - 10 / 2") == 14
    assert evaluate_expression("-2+1") == -1
    assert evaluate_expression("2*(5+5*2)/3+(6/2+8)") == 21