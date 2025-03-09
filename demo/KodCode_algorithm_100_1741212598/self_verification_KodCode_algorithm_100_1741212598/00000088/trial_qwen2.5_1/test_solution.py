from solution import *

import pytest

def test_running_key_cipher_encrypt():
    key = "HOWDOTHEDUCKKNOWTHATCHATSsaidVictor"
    plaintext = "DEFENDTHISTHROUGHPLUNDER"
    ciphertext = running_key_encrypt(key, plaintext)
    assert ciphertext == "HTHOEJPJVUGQRTVEPN"

def test_running_key_cipher_decrypt():
    key = "HOWDOTHEDUCKKNOWTHATCHATSsaidVictor"
    ciphertext = "HTHOEJPJVUGQRTVEPN"
    decrypted_text = running_key_decrypt(key, ciphertext)
    assert decrypted_text == "DEFENDTHISTHROUGHPLUNDER"

def test_running_key_cipher_encrypt_and_decrypt():
    key = "HOWDOTHEDUCKKNOWTHATCHATSsaidVictor"
    message = "DEFENDTHISTHROUGHPLUNDER"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, message)
    assert ciphertext == "HTHOEJPJVUGQRTVEPN"
    assert decrypted_text == "DEFENDTHISTHROUGHPLUNDER"

def test_running_key_cipher_with_mixed_case():
    key = "HELLOWORLD"
    plaintext = "The quick brown fox"
    ciphertext = running_key_encrypt(key, plaintext)
    assert ciphertext == "ADXWUTSYFACBA"

def test_running_key_cipher_with_special_chars():
    key = "ABCDEF"
    plaintext = "Hello, World!"
    ciphertext = running_key_encrypt(key, plaintext)
    assert ciphertext == "PTMMO, BBPMD!"

def test_running_key_cipher_with_empty_key():
    key = ""
    plaintext = "Hello, World!"
    with pytest.raises(ValueError):
        running_key_encrypt(key, plaintext)

def test_running_key_cipher_with_empty_message():
    key = "HELLO"
    plaintext = ""
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, plaintext)
    assert ciphertext == ""
    assert decrypted_text == ""