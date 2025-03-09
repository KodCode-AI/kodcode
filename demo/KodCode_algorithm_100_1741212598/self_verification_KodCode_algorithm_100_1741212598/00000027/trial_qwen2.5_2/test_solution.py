from solution import *

from solution import encrypt_message, decrypt_message

def test_encrypt_decrypt_cycle():
    key = 'HDarji'
    message = 'This is Harshil Darji from Dharmaj.'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message

def test_encrypt_uppercase():
    key = 'XYZ'
    message = 'HELLO WORLD!'
    encrypted = encrypt_message(key, message)
    assert encrypted == 'JXSSO XWPSG!'

def test_decrypt_uppercase():
    key = 'XYZ'
    message = 'JXSSO XWPSG!'
    decrypted = decrypt_message(key, message)
    assert decrypted == 'HELLO WORLD!'

def test_encrypt_mixed_case():
    key = 'abc'
    message = 'Th3s 1s mY Te4st !n p0ind3nT'
    encrypted = encrypt_message(key, message)
    assert encrypted == 'Xi4u 4t tT 9p8py9 4n $0ajivn!'

def test_decrypt_mixed_case():
    key = 'abc'
    message = 'Xi4u 4t tT 9p8py9 4n $0ajivn!'
    decrypted = decrypt_message(key, message)
    assert decrypted == 'Th3s 1s mY Te4st !n p0ind3nT'

def test_encrypt_punctuation():
    key = '012'
    message = 'Test, case: !?, has, 12345.'
    encrypted = encrypt_message(key, message)
    assert encrypted == 'Xpgx, aujf: &?k, p0156.,'

def test_decrypt_punctuation():
    key = '012'
    message = 'Xpgx, aujf: &?k, p0156.,'
    decrypted = decrypt_message(key, message)
    assert decrypted == 'Test, case: !?, has, 12345.'

def test_empty_key():
    key = ''
    message = 'Test Message'
    encrypted = encrypt_message(key, message)
    assert encrypted == 'Test Message'
    decrypted = decrypt_message(key, message)
    assert decrypted == 'Test Message'

def test_empty_message():
    key = 'abc'
    message = ''
    encrypted = encrypt_message(key, message)
    assert encrypted == ''
    decrypted = decrypt_message(key, message)
    assert decrypted == ''

def test_large_key():
    key = 'VeryLongKeyVeryLongKeyVeryLongKeyVeryLongKey'
    message = 'This is a test message.'
    encrypted = encrypt_message(key, message)
    decrypted = decrypt_message(key, encrypted)
    assert decrypted == message