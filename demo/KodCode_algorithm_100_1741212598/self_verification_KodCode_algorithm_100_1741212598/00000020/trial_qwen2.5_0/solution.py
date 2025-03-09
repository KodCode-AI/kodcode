from math import gcd

def are_digit_cancelling_fraction(numerator, denominator):
    """
    Checks if the given fraction is a non-trivial digit-cancelling fraction.
    """
    num_str = str(numerator)
    den_str = str(denominator)
    
    if len(num_str) != 2 or len(den_str) != 2:
        return False
    
    if num_str[1] == '0' and den_str[1] == '0':
        return False
    
    if num_str[0] == den_str[1]:
        if int(num_str[1]) == 0 or int(den_str[0]) * int(num_str[1]) == int(den_str[1]) * int(num_str[0]):
            return True
    if num_str[1] == den_str[0]:
        if int(num_str[0]) == 0 or int(den_str[1]) * int(num_str[0]) == int(den_str[0]) * int(num_str[1]):
            return True
    
    return False

def solution(n: int) -> int:
    if n == 2:
        result = 1
        for num in range(10, 100):
            for den in range(num + 1, 100):
                if are_digit_cancelling_fraction(num, den):
                    result *= den
                    result //= gcd(result, den)
        return result

    elif n == 3:
        result = 1
        for num in range(100, 1000):
            for den in range(num + 1, 1000):
                if are_digit_cancelling_fraction(num, den):
                    common_divisor = gcd(num, den)
                    simplified_den = den // common_divisor
                    result *= simplified_den
                    result //= gcd(result, simplified_den)
        return result

    else:
        raise ValueError("The input 'n' must be either 2 or 3.")