from math import gcd

def is_digit_cancelling_fraction(numerator, denominator):
    """
    Checks if the given fraction is a digit-cancelling fraction.
    """
    num_str = str(numerator)
    den_str = str(denominator)
    for digit in num_str:
        if digit in den_str:
            num_str = num_str.replace(digit, '', 1)
            den_str = den_str.replace(digit, '', 1)
            if den_str:
                new_numerator = int(num_str)
                new_denominator = int(den_str)
                if numerator * new_denominator == denominator * new_numerator:
                    return True
    return False

def product_of_denominators(n: int) -> int:
    """
    Generates non-trivial digit-cancelling fractions for fractions with n digits
    in the numerator and denominator and returns the product of the denominators
    in their lowest terms.
    """
    product = 1
    for numerator in range(10**(n-1), 10**n):
        for denominator in range(numerator + 1, 10**n):
            if is_digit_cancelling_fraction(numerator, denominator):
                product *= denominator
                product //= gcd(product, denominator)  # Simplify the product
    return product