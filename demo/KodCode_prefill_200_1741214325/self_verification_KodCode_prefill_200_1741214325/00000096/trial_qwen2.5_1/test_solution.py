from solution import *

def test_arithmetic_eval():
    assert arithmetic_eval("1 + 2 * 3") == 7
    assert arithmetic_eval("(1 + 2) * 3 - 4") == 3
    assert arithmetic_eval("4 - (2 * (1 + 1))") == 0
    assert arithmetic_eval("2 * 3 + 1") == 7
    assert arithmetic_eval("2 - 3 + 1") == 0
    assert arithmetic_eval("2 * (3 + 1) - 4") == 4