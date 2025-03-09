def custom_dencrypt(s: str, n: int = 13) -> str:
    """
    Encrypts or decrypts the string s using a custom ROT13 variant with a shift of n.
    """
    result = []
    for char in s:
        if char.isalpha():
            shift = n
            base = ord('A') if char.isupper() else ord('a')
            offset = ord(char) - base
            new_offset = (offset + shift) % 26
            result.append(chr(base + new_offset))
        else:
            result.append(char)
    return ''.join(result)

def main():
    s0 = input("Enter message: ")

    try:
        shift = int(input("Enter shift value (1-26): "))
        if not (1 <= shift <= 26):
            print("Shift value must be between 1 and 26.")
            return

        s1 = custom_dencrypt(s0, shift)
        print("Encryption:", s1)

        s2 = custom_dencrypt(s1, shift)
        print("Decryption: ", s2)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 26.")