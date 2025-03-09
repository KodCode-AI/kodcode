from solution import *

from solution import evaluate_infix_expression

def test_infix_evaluation():
    assert evaluate_infix_expression("12 + 22 * (44 - 23)") == 330
    assert evaluate_infix_expression("1 + 2 * 3") == 7
    assert evaluate_infix_expression("1 + 2 * 3 + 4") == 9
    assert evaluate_infix_expression("(1 + 2 + 3) * 4") == 24
    assert evaluate_infix_expression("10 * 2 - 3 + 5") == 22
    assert evaluate_infix_expression("100 * 2 / 2 / 5") == 20
    assert evaluate_infix_expression("(10 + 5) * 2") == 30
    assert evaluate_infix_expression("20 + (5 - 3) * 2") == 24
    assert evaluate_infix_expression("100 + 20 / 10") == 120
    assert evaluate_infix_expression("3 + 2 - 4 / 2") == 2
    assert evaluate_infix_expression("5 - (2 + 2)") == 1
    assert evaluate_infix_expression("(1 + 2) * (3 - 4)") == -3