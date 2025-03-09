def running_key_cipher(key: str, message: str, encrypt=True) -> str:
    """
    Encrypts or decrypts the message using the Running Key Cipher.
    """
    key = key.upper()
    message = message.upper()
    result = ""
    key_index = 0
    
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if encrypt:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    
    return result

def running_key_encrypt(key: str, plaintext: str) -> str:
    """
    Encrypts the plaintext using the Running Key Cipher.
    """
    return running_key_cipher(key, plaintext, encrypt=True)

def running_key_decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts the ciphertext using the Running Key Cipher.
    """
    return running_key_cipher(key, ciphertext, encrypt=False)

def running_key_encrypt_and_decrypt(key: str, message: str) -> (str, str):
    """
    Encrypts and then decrypts the message to ensure the original message is recovered.
    """
    ciphertext = running_key_encrypt(key, message)
    decrypted_text = running_key_decrypt(key, ciphertext)
    return ciphertext, decrypted_text