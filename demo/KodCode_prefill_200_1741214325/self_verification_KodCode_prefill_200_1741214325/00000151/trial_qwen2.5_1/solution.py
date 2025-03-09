To convert a decimal number to binary without using Python's built-in `bin()` function, we can use the following approach:

1. Define a function `decimal_to_binary` that takes a decimal number as input.
2. Initialize an empty string to store the binary representation.
3. Use a while loop to divide the decimal number by 2 and get the remainder. Append the remainder to the string.
4. Continue the process until the decimal number becomes 0.
5. Reverse the string of remainders to get the correct binary representation.

def decimal_to_binary(decimal_number):
    """
    Converts a decimal number to binary without using Python's built-in bin() function.
    """
    if decimal_number == 0:
        return "0"
    
    binary = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary += str(remainder)
        decimal_number = decimal_number // 2
    
    return binary[::-1]