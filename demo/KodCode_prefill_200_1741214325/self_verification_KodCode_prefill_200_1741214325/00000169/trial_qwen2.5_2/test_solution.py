from solution import *

from solution import evaluate_postfix

def test_evaluate_postfix_positive():
    assert evaluate_postfix("3 4 +") == 7
    assert evaluate_postfix("5 1 2 + 4 * + 3 -") == 14

def test_evaluate_postfix_with_negative():
    assert evaluate_postfix("10 2 / 3 - 5 +") == 2
    assert evaluate_postfix("-1 2 *") == -2

def test_evaluate_postfix_zero():
    assert evaluate_postfix("4 -4 -") == 0
    assert evaluate_postfix("0 0 +") == 0
    assert evaluate_postfix("0 -0 +") == 0

def test_evaluate_postfix_single_number():
    assert evaluate_postfix("7") == 7

def test_evaluate_postfix_division_behavior():
    assert evaluate_postfix("10 5 /") == 2
    assert evaluate_postfix("10 5 / 2 -") == 0

def test_evaluate_postfix_invalid_expression():
    with pytest.raises(ValueError):
        evaluate_postfix("4 2 + x")
    with pytest.raises(ValueError):
        evaluate_postfix("10 / 0")
    with pytest.raises(ValueError):
        evaluate_postfix("10 2 3 +")