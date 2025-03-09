def encrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, "encrypt")

def decrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, "decrypt")

def translate_message(key: str, message: str, mode: str) -> str:
    translated = []
    key_index = 0
    for char in message:
        num = LETTERS.find(char)
        if num != -1:
            if mode == "encrypt":
                new_index = (num + LETTERS.find(key[key_index])) % 63
            elif mode == "decrypt":
                new_index = (num - LETTERS.find(key[key_index])) % 63
            translated.append(LETTERS[new_index])
            key_index = (key_index + 1) % len(key)
        else:
            translated.append(char)
    return "".join(translated)