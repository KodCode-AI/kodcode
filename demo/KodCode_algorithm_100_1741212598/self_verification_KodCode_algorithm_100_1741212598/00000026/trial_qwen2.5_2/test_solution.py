from solution import *

from solution import custom_dencrypt, main

# Test custom_dencrypt function
def test_custom_dencrypt():
    assert custom_dencrypt("Hello, World!", 13) == "Uryyb, Jbeyq!"
    assert custom_dencrypt("Uryyb, Jbeyq!", 13) == "Hello, World!"
    assert custom_dencrypt("abc", 3) == "def"
    assert custom_dencrypt("Abc", 3) == "Def"
    assert custom_dencrypt("123", 5) == "123"
    assert custom_dencrypt("AaBbCc", 26) == "AaBbCc"
    assert custom_dencrypt("AaBbCc", 0) == "Invalid shift value. It must be between 1 and 26."
    assert custom_dencrypt("AaBbCc", 27) == "Invalid shift value. It must be between 1 and 26."

# Test main function
def test_main():
    # Redirect input and output for testing
    from io import StringIO
    import sys
    inputs = ["Hello, World!\n", "13\n"]
    outputs = ["Encryption: Uryyb, Jbeyq!\nDecryption:  Hello, World!\n"]

    sys.stdin = StringIO("".join(inputs))
    sys.stdout = StringIO()

    main()
    sys.stdout.seek(0)
    assert sys.stdout.read() == "".join(outputs)

    sys.stdin.seek(0)
    sys.stdout.seek(0)
    sys.stdout.truncate(0)
    inputs[1] = "27\n"
    main()
    sys.stdout.seek(0)
    assert sys.stdout.read() == "Shift value must be between 1 and 26.\n"
    
    sys.stdin.seek(0)
    sys.stdout.seek(0)
    sys.stdout.truncate(0)
    inputs[1] = "-5\n"
    main()
    sys.stdout.seek(0)
    assert sys.stdout.read() == "Shift value must be between 1 and 26.\n"

    sys.stdin.seek(0)
    sys.stdout.seek(0)
    sys.stdout.truncate(0)
    inputs[1] = "a\n"
    main()
    sys.stdout.seek(0)
    assert sys.stdout.read() == "Invalid input. Please enter a number between 1 and 26.\n"

    sys.stdin.seek(0)
    sys.stdout.seek(0)
    sys.stdout.truncate(0)
    inputs[1] = "1\n"
    main()
    sys.stdout.seek(0)
    assert sys.stdout.read() == "Encryption: Ifmmp, Xpsme!\nDecryption:  Hello, World!\n"