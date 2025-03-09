def generate_table(key: str) -> list:
    """
    Generates a 5x5 Playfair matrix using the given key and removing non-alphabetic characters.
    """
    key = ''.join(filter(str.isalpha, key.upper()))
    key = key.replace("J", "I")  # Replace J with I as both are represented by I in the Playfair cipher
    table = []

    for char in key:
        if char not in ''.join(table):
            table.append(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # Skip 'J' as it's covered by 'I'
        if char not in table:
            table.append(char)

    return [table[i:i+5] for i in range(0, 25, 5)]


def find_position(table: list, char: str) -> tuple:
    """
    Finds the position (row, col) of a character in the Playfair matrix.
    """
    for i, row in enumerate(table):
        for j, val in enumerate(row):
            if val == char:
                return i, j


def advanced_encrypt(key: str, text: str) -> str:
    """
    Encrypts the text using the Playfair cipher with the given key.
    """
    table = generate_table(key)
    text = text.upper()
    text = text.replace("J", "I")  # Replace J with I
    spaced_text = [''.join(text[i:i+2]) for i in range(0, len(text), 2)]

    for i, pair in enumerate(spaced_text):
        if len(pair) < 2:
            spaced_text[i] += 'X'  # Fill missing character with 'X'

    cipher_text = ''.join([table[row1][col1] + table[row2][col2] if row1 == row2 or col1 == col2 else table[row1][col2] + table[row2][col1] for (row1, col1), (row2, col2) in [(find_position(table, char1), find_position(table, char2)) for char1, char2 in zip(*[iter(spaced_text)]*2)]])

    return cipher_text


def advanced_decrypt(key: str, cipher_text: str) -> str:
    """
    Decrypts the text using the Playfair cipher with the given key.
    """
    table = generate_table(key)
    cipher_text = cipher_text.upper()
    cipher_text = cipher_text.replace("J", "I")  # Replace J with I
    cipher_text = ''.join([cipher_text[i:i+2] for i in range(0, len(cipher_text), 2)])

    plain_text = ''.join([table[row1][col1] + table[row2][col2] if row1 == row2 or col1 == col2 else table[row2][col1] + table[row1][col2] for (row1, col1), (row2, col2) in [(find_position(table, char1), find_position(table, char2)) for char1, char2 in zip(cipher_text[::2], cipher_text[1::2])]])

    # Remove added 'X' characters
    returned_text = []
    i = 0
    while i < len(plain_text):
        if plain_text[i] == plain_text[i+1]:
            returned_text.append(plain_text[i])
            i += 1
        else:
            returned_text.append(plain_text[i:i+2])
            i += 2

    return ''.join(returned_text)


key = "MARVIN"
text = "jessica!123"

encrypted_text = advanced_encrypt(key, text)
decrypted_text = advanced_decrypt(key, encrypted_text)

print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")