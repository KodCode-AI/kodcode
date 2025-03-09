def generate_table(key: str) -> list:
    """
    Generates a 5x5 matrix (Playfair cipher table) from the given key.
    Non-alphabetic characters in the key are ignored.
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper().replace('J', 'I')  # Convert to uppercase and replace J with I
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates and maintain order
    table = [list(key[i:i+5]) for i in range(0, len(key), 5)]
    for letter in alphabet:
        if letter not in key:
            if letter == 'J':
                continue
            table[int(len(table) - 1)].append(letter)
    return table

def find_position(table: list, letter: str) -> tuple:
    """
    Finds the position (row, col) of a letter in the table.
    """
    for i in range(5):
        for j in range(5):
            if table[i][j] == letter:
                return i, j

def advanced_encrypt(key: str, text: str) -> str:
    """
    Encrypts the text using the Playfair cipher with the given key.
    """
    table = generate_table(key)
    text = text.upper().replace('J', 'I')  # Convert to uppercase and replace J with I
    text = ''.join(filter(str.isalpha, text))  # Remove non-alphabetic characters
    encrypted = ""
    for i in range(0, len(text), 2):
        if i + 1 == len(text):
            encrypted += text[i] + 'X'
        else:
            first, second = text[i], text[i + 1]
            pos1, pos2 = find_position(table, first), find_position(table, second)
            if pos1[0] == pos2[0]:  # Same row
                encrypted += table[pos1[0]][(pos1[1] + 1) % 5] + table[pos2[0]][(pos2[1] + 1) % 5]
            elif pos1[1] == pos2[1]:  # Same column
                encrypted += table[(pos1[0] + 1) % 5][pos1[1]] + table[(pos2[0] + 1) % 5][pos2[1]]
            else:  # Different row and column
                encrypted += table[pos1[0]][pos2[1]] + table[pos2[0]][pos1[1]]
    return encrypted

def advanced_decrypt(key: str, cipher_text: str) -> str:
    """
    Decrypts the cipher text using the Playfair cipher with the given key.
    """
    table = generate_table(key)
    cipher_text = cipher_text.upper().replace('J', 'I')  # Convert to uppercase and replace J with I
    decrypted = ""
    for i in range(0, len(cipher_text), 2):
        first, second = cipher_text[i], cipher_text[i + 1]
        pos1, pos2 = find_position(table, first), find_position(table, second)
        if pos1[0] == pos2[0]:  # Same row
            decrypted += table[pos1[0]][(pos1[1] - 1) % 5] + table[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:  # Same column
            decrypted += table[(pos1[0] - 1) % 5][pos1[1]] + table[(pos2[0] - 1) % 5][pos2[1]]
        else:  # Different row and column
            decrypted += table[pos1[0]][pos2[1]] + table[pos2[0]][pos1[1]]
    return decrypted[:-1]  # Remove the last character (X) if present