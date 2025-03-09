from solution import *

import pytest

def test_custom_dencrypt_uppercase():
    assert custom_dencrypt("ABC", 3) == "DEF"
    assert custom_dencrypt("DEF", 3) == "ABC"

def test_custom_dencrypt_lowercase():
    assert custom_dencrypt("abc", 3) == "def"
    assert custom_dencrypt("def", 3) == "abc"

def test_custom_dencrypt_mixed():
    assert custom_dencrypt("Hello, World!", 13) == "Uryyb, Jbeyq!"

def test_custom_dencrypt_non_alpha():
    assert custom_dencrypt("1234!@#$", 13) == "1234!@#$"

def test_custom_dencrypt_edge_cases():
    assert custom_dencrypt("Z", 1) == "A"
    assert custom_dencrypt("z", 1) == "a"
    assert custom_dencrypt("A", 26) == "A"
    assert custom_dencrypt("a", 26) == "a"
    
def test_custom_dencrypt_invalid_shift():
    with pytest.raises(ValueError):
        custom_dencrypt("test", 27)