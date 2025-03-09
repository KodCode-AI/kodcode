from solution import *

def test_encrypt_decrypt_cycle():
    key = 'HDarji'
    message = 'This is Harshil Darji from Dharmaj.'
    encrypted_message = encrypt_message(key, message)
    decrypted_message = decrypt_message(key, encrypted_message)
    assert decrypted_message == message

def test_case_maintenance():
    key = 'HDarji'
    message = 'T3st, MiXed! 123'
    translated_message = translate_message(key, message, 'encrypt')
    assert translated_message.isalnum() or translated_message.isalpha() or all(c in ' ,!?' for c in translated_message)

def test_punctuation():
    key = 'HDarji'
    message = 'Hello, World!'
    encrypted_message = translate_message(key, message, 'encrypt')
    assert encrypted_message.startswith('Akij, Lloq!')

def testspecialchars():
    key = 'HDarji'
    message = 'Special $%^&*() Characters'
    encrypted_message = translate_message(key, message, 'encrypt')
    assert encrypted_message.startswith('Dnqrbt $%^&*() Characters')

def test_long_message():
    key = 'SimpleKey'
    message = 'A quick brown fox jumps over the lazy dog. 0123456789'
    encrypted_message = translate_message(key, message, 'encrypt')
    decrypted_message = translate_message(key, encrypted_message, 'decrypt')
    assert decrypted_message == message

def test_empty_message():
    key = 'HDarji'
    message = ''
    assert translate_message(key, message, 'encrypt') == ''
    assert translate_message(key, message, 'decrypt') == ''

def test_spaces():
    key = 'HDarji'
    message = 'Some Random Text   Spaces    '
    translated_message = translate_message(key, message, 'encrypt')
    assert 'J vlu Ftvzvh Ayow     )vkhq      ' in translated_message