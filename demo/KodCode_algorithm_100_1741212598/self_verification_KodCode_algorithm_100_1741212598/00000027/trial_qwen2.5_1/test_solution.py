from solution import *

from solution import encrypt_message, decrypt_message, LETTERS

def test_encrypt_decrypt_roundtrip():
    key = 'HDarji'
    message = 'This is Harshil Darji from Dharmaj.'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_encryption():
    key = 'HDarji'
    message = 'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    encrypted = encrypt_message(key, message)
    assert encrypted == 'This is Harshil Darji from Dharmaj.'

def test_decryption():
    key = 'HDarji'
    message = 'This is Harshil Darji from Dharmaj.'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_spaces_and_punctuation():
    key = 'HDarji'
    message = 'Hello, World!'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_case_maintenance():
    key = 'HDarji'
    message = 'This Is Test Message!'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_caps_and_special_chars():
    key = 'HDarji'
    message = 'This Is A Test Message!!!'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_small_key():
    key = 'A'
    message = 'This is a test message.'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_large_key():
    key = 'HDarjiHDarjiHDarji'
    message = 'This is another test message.'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_empty_key():
    key = ''
    message = 'This is an empty key message.'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message