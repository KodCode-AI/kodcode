from solution import *

from solution import is_fibonacci_number, is_perfect_square

def test_is_perfect_square():
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(25) == True
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(17) == False

def test_is_fibonacci_number():
    assert is_fibonacci_number(0) == True
    assert is_fibonacci_number(1) == True
    assert is_fibonacci_number(5) == True
    assert is_fibonacci_number(8) == True
    assert is_fibonacci_number(13) == True
    assert is_fibonacci_number(21) == True
    assert is_fibonacci_number(34) == True
    assert is_fibonacci_number(55) == True
    assert is_fibonacci_number(6) == False
    assert is_fibonacci_number(-4) == False
    assert is_fibonacci_number(20) == False