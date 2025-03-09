def running_key_cipher(text, key, shift):
    """
    Encrypts or decrypts the text using the running key cipher.
    """
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            # Calculate the shift for the character
            shift_value = ord(key[key_index % len(key)].upper()) - ord('A')
            if shift:
                result += chr((ord(char.upper()) - ord('A') + shift_value) % 26 + ord('A'))
            else:
                result += chr((ord(char.upper()) - ord('A') - shift_value) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result

def running_key_encrypt(key: str, plaintext: str) -> str:
    return running_key_cipher(plaintext, key, True)

def running_key_decrypt(key: str, ciphertext: str) -> str:
    return running_key_cipher(ciphertext, key, False)

def running_key_encrypt_and_decrypt(key: str, message: str) -> (str, str):
    ciphertext = running_key_encrypt(key, message)
    decrypted_text = running_key_decrypt(key, ciphertext)
    return ciphertext, decrypted_text