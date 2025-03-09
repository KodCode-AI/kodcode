def generate_table(key):
    """
    Generates a 5x5 matrix for the Playfair cipher using the given key.
    """
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Excluding 'J' as it is combined with 'I'
    key = key.upper().replace("J", "I")  # Replace 'J' with 'I' and convert to uppercase

    table = []
    for char in key:
        if char not in letters:
            continue
        if char not in table:
            table.append(char)
    for char in letters:
        if char not in table:
            table.append(char)

    # Reshape into a 5x5 matrix
    return [table[i:i+5] for i in range(0, 25, 5)]

def advanced_encrypt(key, text):
    """
    Encrypts the given text using the Playfair cipher with the provided key.
    """
    table = generate_table(key)
    text = text.upper().replace("J", "I").replace(" ", "")  # Convert to uppercase and remove spaces

    i, j = 0, 0
    pairs = []
    while i < len(text):
        c1, c2 = text[i], text[i+1] if i+1 < len(text) else 'X'  # Use 'X' as filler if needed
        i1, j1 = -1, -1
        i2, j2 = -1, -1

        for r in range(5):
            for c in range(5):
                if table[r][c] == c1:
                    i1, j1 = r, c
                if table[r][c] == c2:
                    i2, j2 = r, c

        if i1 == j1:  # Same row
            i1, i2 = (i1 + 1) % 5, (i2 + 1) % 5
        elif i2 == j2:  # Same column
            i1, i2 = (i1 + 1) % 5, (i2 + 1) % 5
        else:  # Different row and column
            i1, j1, i2, j2 = i2, j1, i1, j2

        pairs.append(table[i1][j1] + table[i2][j2])
        i += 2

    return ''.join(pairs)

def advanced_decrypt(key, cipher_text):
    """
    Decrypts the given text using the Playfair cipher with the provided key.
    """
    table = generate_table(key)
    cipher_text = cipher_text.upper().replace("J", "I")  # Convert to uppercase and replace 'J' with 'I'

    i, j = 0, 0
    pairs = []
    while i < len(cipher_text):
        c1, c2 = cipher_text[i], cipher_text[i+1] if i+1 < len(cipher_text) else 'X'  # Use 'X' as filler if needed
        i1, j1 = -1, -1
        i2, j2 = -1, -1

        for r in range(5):
            for c in range(5):
                if table[r][c] == c1:
                    i1, j1 = r, c
                if table[r][c] == c2:
                    i2, j2 = r, c

        if i1 == j1:  # Same row
            i1, i2 = (i1 - 1) % 5, (i2 - 1) % 5
        elif i2 == j2:  # Same column
            i1, i2 = (i1 - 1) % 5, (i2 - 1) % 5
        else:  # Different row and column
            i1, j1, i2, j2 = i2, j1, i1, j2

        pairs.append(table[i1][j1] + table[i2][j2])
        i += 2

    return ''.join(pairs).replace("XX", "X").replace("X", " ")  # Restore spaces and remove double 'X'