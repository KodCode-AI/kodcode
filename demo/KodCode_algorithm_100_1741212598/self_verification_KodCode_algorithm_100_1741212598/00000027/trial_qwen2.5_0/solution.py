def encrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, "encrypt")

def decrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, "decrypt")

def translate_message(key: str, message: str, mode: str) -> str:
    # Build encrypted/decrypted message string
    translated = []

    key_index = 0
    for symbol in message:
        num = LETTERS.find(symbol)
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index % len(key)])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index % len(key)])
            
            num %= len(LETTERS)
            
            if symbol.isupper():
                translated.append(LETTERS[num].upper())
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            elif symbol in ' .,!?':
                translated.append(symbol)
            else:
                translated.append(LETTERS[num])
            
            key_index += 1
        else:
            translated.append(symbol)  # For non-letter characters

    return ''.join(translated)