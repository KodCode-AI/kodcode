from solution import *

from solution import evaluate_postfix

def test EvaluatePostfix_valid_input():
    assert evaluate_postfix("3 4 + 2 * 7 /") == 2
    assert evaluate_postfix("10 2 8 * + 100 2 / -") == 90

def test EvaluatePostfix_single_number():
    assert evaluate_postfix("5") == 5

def test EvaluatePostfix_no_operand():
    with pytest.raises(ValueError):
        evaluate_postfix("3 +")

def test EvaluatePostfix_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate_postfix("1 0 /")

def test EvaluatePostfix_invalid_expression():
    with pytest.raises(ValueError):
        evaluate_postfix("3 4 6 +")
    with pytest.raises(ValueError):
        evaluate_postfix("3 a +")
    with pytest.raises(ValueError):
        evaluate_postfix("10 2 / 10 -")