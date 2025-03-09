def custom_dencrypt(s: str, n: int = 13) -> str:
    """
    Encrypts or decrypts the given string using the custom ROT13 variant with a shift of n.
    """
    if not 1 <= n <= 26:
        raise ValueError("Shift value must be between 1 and 26.")
    
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = n if char.islower() else -n
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted += new_char
        else:
            encrypted += char
    return encrypted

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