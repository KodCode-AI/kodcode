from solution import *

from solution import generate_table, advanced_encrypt, advanced_decrypt

def test_generate_table():
    key = "MCRY"
    table = generate_table(key)
    expected_table = [
        ['M', 'C', 'R', 'Y', 'B'],
        ['A', 'D', 'E', 'F', 'G'],
        ['H', 'I', 'K', 'L', 'N'],
        ['O', 'P', 'Q', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Z']
    ]
    assert table == expected_table

def test_advanced_encrypt():
    key = "MCRY"
    text = "jessica!123"
    encrypted_text = advanced_encrypt(key, text)
    assert encrypted_text == "QRACRWU!123"

def test_advanced_decrypt():
    key = "MCRY"
    text = "QRACRWU!123"
    decrypted_text = advanced_decrypt(key, text)
    assert decrypted_text == "JESSICA!123"

def test_advanced_encrypt_empty_string():
    key = "MCRY"
    text = ""
    encrypted_text = advanced_encrypt(key, text)
    assert encrypted_text == ""

def test_advanced_decrypt_empty_string():
    key = "MCRY"
    text = ""
    decrypted_text = advanced_decrypt(key, text)
    assert decrypted_text == ""

def test_advanced_encrypt_with_non_alpha_chars():
    key = "MCRY"
    text = "j3ss1c4!"
    encrypted_text = advanced_encrypt(key, text)
    assert encrypted_text == "QRA3RWU!"

def test_advanced_decrypt_with_non_alpha_chars():
    key = "MCRY"
    text = "QRA3RWU!"
    decrypted_text = advanced_decrypt(key, text)
    assert decrypted_text == "J3SS1C4!"

def test_advanced_encrypt_with_key_containing_non_alpha_chars():
    key = "M2CRY"
    text = "j3ss1c4!"
    encrypted_text = advanced_encrypt(key, "Z" + text)  # Adding 'Z' to ensure key validity
    assert encrypted_text == "QRA3RWU!"

def test_advanced_decrypt_with_key_containing_non_alpha_chars():
    key = "M2CRY"
    text = "QRA3RWU!"
    decrypted_text = advanced_decrypt(key, "Z" + text)  # Adding 'Z' to ensure key validity
    assert decrypted_text == "J3SS1C4!"