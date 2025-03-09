from solution import *

import pytest

def test_custom_dencrypt_single_character():
    assert custom_dencrypt("A", 13) == "N"
    assert custom_dencrypt("N", 13) == "A"
    assert custom_dencrypt("a", 13) == "n"
    assert custom_dencrypt("n", 13) == "a"

def test_custom_dencrypt_uppercase():
    assert custom_dencrypt("Hello World!", 13) == "Uryyb Jbeyq!"
    assert custom_dencrypt("Uryyb Jbeyq!", 13) == "Hello World!"

def test_custom_dencrypt_lowercase():
    assert custom_dencrypt("hello world!", 13) == "uryyb jbeyq!"
    assert custom_dencrypt("uryyb jbeyq!", 13) == "hello world!"

def test_custom_dencrypt_mixed():
    assert custom_dencrypt("Hello, World!", 13) == "Uryyb, Jbeyq!"
    assert custom_dencrypt("Uryyb, Jbeyq!", 13) == "Hello, World!"

def test_custom_dencrypt_non_alpha():
    assert custom_dencrypt("Hello,123!", 13) == "Uryyb,123!"
    assert custom_dencrypt("Uryyb,123!", 13) == "Hello,123!"

def test_custom_dencrypt_shift_error():
    with pytest.raises(AssertionError):
        assert custom_dencrypt("Hello", 0)

def test_custom_dencrypt_shift_out_of_range():
    with pytest.raises(AssertionError):
        assert custom_dencrypt("Hello", 27)