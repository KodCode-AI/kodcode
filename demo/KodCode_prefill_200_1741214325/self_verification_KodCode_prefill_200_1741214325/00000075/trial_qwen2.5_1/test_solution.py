from solution import *

from solution import is_perfect_number

def test_is_perfect_number_six():
    assert is_perfect_number(6) == True

def test_is_perfect_number_twenty_eight():
    assert is_perfect_number(28) == True

def test_is_not_perfect_number_four():
    assert is_perfect_number(4) == False

def test_is_not_perfect_number_negative_numbers():
    assert is_perfect_number(-6) == False

def test_is_not_perfect_number_zero():
    assert is_perfect_number(0) == False

def test_is_not_perfect_number_one():
    assert is_perfect_number(1) == False

def test_is_not_perfect_number_large_number():
    assert is_perfect_number(496) == True
    assert is_perfect_number(8128) == True
    assert is_perfect_number(33550336) == True
    assert is_perfect_number(8589869056) == True
    assert is_perfect_number(137438691328) == True
    assert is_perfect_number(2305843008139952128) == True

def test_is_not_perfect_number_other_numbers():
    assert is_perfect_number(5) == False
    assert is_perfect_number(10) == False
    assert is_perfect_number(15) == False
    assert is_perfect_number(18) == False
    assert is_perfect_number(20) == False
    assert is_perfect_number(21) == False