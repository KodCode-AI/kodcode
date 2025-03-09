from solution import *

from solution import running_key_encrypt, running_key_decrypt, running_key_encrypt_and_decrypt

def test_running_key_cipher():
    assert running_key_cipher("HOW", "defend", encrypt=True) == "fugqh"
    assert running_key_cipher("HOW", "fugqh", encrypt=False) == "DEFEND"

def test_running_key_encrypt():
    key = "HOW DOES THE DUCK KNOW THAT? SAID VICTOR"
    plaintext = "DEFEND THIS"
    ciphertext = running_key_encrypt(key, plaintext)
    assert ciphertext == "FUGQHUBKH"

def test_running_key_decrypt():
    key = "HOW DOES THE DUCK KNOW THAT? SAID VICTOR"
    ciphertext = "FUGQHUBKH"
    plaintext = running_key_decrypt(key, ciphertext)
    assert plaintext == "DEFEND THIS"

def test_running_key_encrypt_and_decrypt():
    key = "HOW DOES THE DUCK KNOW THAT? SAID VICTOR"
    message = "DEFEND THIS"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, message)
    assert ciphertext == "FUGQHUBKH"
    assert decrypted_text == "DEFEND THIS"

def test_edge_cases():
    key = "A A A A A"
    plaintext = "TEXT"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, plaintext)
    assert ciphertext == "UVWX"
    assert decrypted_text == "TEXT"

    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, plaintext)
    assert ciphertext == "ZABCDEFGHIJKLMNOPQRSTUVWXY"
    assert decrypted_text == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key = ""
    plaintext = "A"
    assert running_key_encrypt(key, plaintext) == "A"
    assert running_key_decrypt(key, "A") == "A"