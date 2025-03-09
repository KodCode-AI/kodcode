from solution import *

python
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True
    assert is_prime(20) == False
    assert is_prime(23) == True
    assert is_prime(25) == False
    assert is_prime(29) == True
    assert is_prime(97) == True
    assert is_prime(100) == False
    assert is_prime(101) == True
    assert is_prime(102) == False
    assert is_prime(103) == True
    assert is_prime(104) == False
    assert is_prime(105) == False
    assert is_prime(106) == False
    assert is_prime(107) == True
    assert is_prime(108) == False
    assert is_prime(109) == True
    assert is_prime(110) == False

def test_special_cases():
    assert is_prime(1) == False
    assert is_prime(-7) == False
    assert is_prime(0) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False

def test_large_numbers():
    assert is_prime(982451653) == True  # Known prime number
    assert is_prime(982451654) == False # Known composite number
    assert is_prime(1234567891) == True # Known prime number
    assert is_prime(1234567890) == False# Known composite number