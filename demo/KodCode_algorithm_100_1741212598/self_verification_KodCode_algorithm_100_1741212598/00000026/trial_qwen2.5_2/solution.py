def custom_dencrypt(s: str, n: int = 13) -> str:
    """
    Returns the string encrypted or decrypted using the custom ROT13 variant with a shift of n.
    """
    if n < 1 or n > 26:
        return "Invalid shift value. It must be between 1 and 26."
    
    def shift_char(c: str, base: int) -> str:
        offset = ord(c) - base
        shifted_offset = (offset + n) % 26
        return chr(base + shifted_offset)

    encrypted = []
    for char in s:
        if 'a' <= char <= 'z':
            encrypted.append(shift_char(char, ord('a')))
        elif 'A' <= char <= 'Z':
            encrypted.append(shift_char(char, ord('A')))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def main():
    s0 = input("Enter message: ")

    try:
        shift = int(input("Enter shift value (1-26): "))
        if 1 <= shift <= 26:
            s1 = custom_dencrypt(s0, shift)
            print("Encryption:", s1)

            s2 = custom_dencrypt(s1, shift)
            print("Decryption: ", s2)
        else:
            print("Shift value must be between 1 and 26.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 26.")