from solution import *

`python
def test_running_key_cipher():
    key = "How does the duck know that? said Victor"
    plaintext = "DEFEND THIS"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, plaintext)
    assert ciphertext == "FUGQHUBKH"
    assert decrypted_text == "DEFEND THIS"

def test_running_key_cipher_with_mixed_case_key():
    key = "hOw d0es tHe duck kn0w tHat? s4id v0c1tor"
    plaintext = "d3f3nd tHi5"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, plaintext)
    assert ciphertext == "fUgQhUbkH"
    assert decrypted_text == "d3f3nd tHi5"

def test_running_key_cipher_with_numbers_and_spaces():
    key = "Quick brown fox jumps over the lazy dogs"
    plaintext = "123 ABC XYZ"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, plaintext)
    assert ciphertext == "F4Q D6S 6RC"
    assert decrypted_text == "123 ABC XYZ"

def test_running_key_cipher_with_long_message():
    key = "This is a long running key that will be used to encrypt a long message"
    plaintext = "The quick brown fox jumps over the lazy dogs"
    ciphertext, decrypted_text = running_key_encrypt_and_decrypt(key, plaintext)
    assert ciphertext == "Hwi U47k4 S022 04lu 3509ow 159w4th 4s 23oa6 T82"
    assert decrypted_text == "The quick brown fox jumps over the lazy dogs"