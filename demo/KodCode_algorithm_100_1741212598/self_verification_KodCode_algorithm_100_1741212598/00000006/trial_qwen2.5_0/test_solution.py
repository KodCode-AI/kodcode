from solution import *

import pytest

def test_generate_table():
    key = "playfair"
    expected_table = [
        ['P', 'L', 'A', 'I', 'R'],
        ['F', 'B', 'C', 'D', 'E'],
        ['G', 'H', 'K', 'M', 'N'],
        ['O', 'Q', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]
    assert generate_table(key) == expected_table

def test_find_position():
    table = generate_table("MARVIN")
    assert find_position(table, 'A') == (0, 1)
    assert find_position(table, 'Z') == (4, 4)

def test_encryption():
    key = "MARVIN"
    text = "jessica!123"
    encrypted_text = "QRACRWU!123"
    assert advanced_encrypt(key, text) == encrypted_text

def test_decryption():
    key = "MARVIN"
    text = "jessica!123"
    encrypted_text = advanced_encrypt(key, text)
    decrypted_text = "JESSICA!123"
    assert advanced_decrypt(key, encrypted_text) == decrypted_text

def test_edge_cases():
    key = "PLAYFAIR"
    text = ""
    encrypted_text = advanced_encrypt(key, text)
    decrypted_text = advanced_decrypt(key, encrypted_text)
    assert encrypted_text == ""
    assert decrypted_text == ""

    key = "PLAYFAIR"
    text = "A"
    encrypted_text = advanced_encrypt(key, text)
    decrypted_text = advanced_decrypt(key, encrypted_text)
    assert encrypted_text == "AE"
    assert decrypted_text == "A"

    key = "PLAYFAIR"
    text = "AB"
    encrypted_text = advanced_encrypt(key, text)
    decrypted_text = advanced_decrypt(key, encrypted_text)
    assert encrypted_text == "AE"
    assert decrypted_text == "AB"

    key = "PLAYFAIR"
    text = "AX"
    encrypted_text = advanced_encrypt(key, text)
    decrypted_text = advanced_decrypt(key, encrypted_text)
    assert encrypted_text == "AEC"
    assert decrypted_text == "AX"