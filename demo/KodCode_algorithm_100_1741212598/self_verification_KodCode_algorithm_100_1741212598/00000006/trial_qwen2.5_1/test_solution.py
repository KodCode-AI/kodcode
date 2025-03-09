from solution import *

import pytest

key = "marvin"
text = "jessica!123"
cipher_text = "QRACRWU!123"

def test_advanced_encrypt_decrypt():
    encrypted = advanced_encrypt(key, text)
    assert encrypted == cipher_text
    decrypted = advanced_decrypt(key, encrypted)
    assert decrypted == text.upper().replace('J', 'I')

def test_non_alphabetic_chars():
    text = "test-123&*()"
    encrypted = advanced_encrypt(key, text)
    assert encrypted == "AIFQH"
    decrypted = advanced_decrypt(key, encrypted)
    assert decrypted == "TEST"

def test_empty_text():
    text = ""
    assert advanced_encrypt(key, text) == ""
    assert advanced_decrypt(key, "") == ""

def test_single_character():
    text = "a"
    encrypted = advanced_encrypt(key, text)
    assert encrypted == "AN"
    decrypted = advanced_decrypt(key, encrypted)
    assert decrypted == "A"

def test_large_text():
    text = "This is a sample text to test the encryption and decryption functionality with a large input. J"
    encrypted = advanced_encrypt(key, text)
    assert len(encrypted) == 92  # Expected length of the encrypted text
    decrypted = advanced_decrypt(key, encrypted)
    assert decrypted == text.upper().replace('J', 'I')