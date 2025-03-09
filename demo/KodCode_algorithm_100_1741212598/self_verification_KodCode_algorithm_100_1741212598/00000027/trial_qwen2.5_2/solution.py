LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!"

def find_position(letter, mode):
    if letter in LETTERS:
        if mode == 'encrypt':
            return LETTERS.find(letter)
        if mode == 'decrypt':
            return LETTERS.rfind(letter)
    return -1

def encrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, "encrypt")

def decrypt_message(key: str, message: str) -> str:
    return translate_message(key, message, "decrypt")

def translate_message(key: str, message: str, mode: str) -> str:
    translation = ""
    key_index = 0
    for char in message:
        if char in LETTERS:
            temp_key = key[key_index % len(key)]
            key_index += 1
            if mode == 'encrypt':
                new_index = (find_position(char, 'encrypt') + find_position(temp_key, 'encrypt')) % len(LETTERS)
            else:  # mode == 'decrypt'
                new_index = (find_position(char, 'decrypt') - find_position(temp_key, 'encrypt')) % len(LETTERS)
            translation += LETTERS[new_index]
        else:
            translation += char
    return translation