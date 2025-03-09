def running_key_encrypt(key: str, plaintext: str) -> str:
    """
    Encrypts the plaintext using the Running Key Cipher.
    """
    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext


def running_key_decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts the ciphertext using the Running Key Cipher.
    """
    key = key.upper()
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext


def running_key_encrypt_and_decrypt(key: str, message: str) -> (str, str):
    """
    Encrypts and then decrypts the message.
    """
    ciphertext = running_key_encrypt(key, message)
    decrypted_text = running_key_decrypt(key, ciphertext)
    return ciphertext, decrypted_text