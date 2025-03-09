def check_opposite_signs(num1, num2):
    """
    Determines if two integers have opposite signs using bitwise operations.
    """
    # Mask to check the sign bit (32nd bit for int32)
    mask = 0x80000000
    
    # XOR the sign bits of both numbers, if the result's sign bit is set, then numbers have opposite signs
    return (num1 & mask) ^ (num2 & mask) == mask