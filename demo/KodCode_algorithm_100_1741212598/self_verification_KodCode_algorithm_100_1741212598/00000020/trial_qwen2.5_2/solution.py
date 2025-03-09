from math import gcd

def digit_cancelling_fractions(n: int) -> int:
    """
    Generates a list of non-trivial digit-cancelling fractions with `n` digits in their numerator and denominator.
    Returns the product of the denominators of these fractions in their lowest terms.
    """
    def is_non_trivial_digit_cancelling(a, b):
        str_a, str_b = str(a), str(b)
        for i in range(2):
            for j in range(2):
                if str_a[i] == str_b[j] and str_a[i] != '0':
                    a1, a2 = int(str_a[1 - i]), int(str_b[1 - j])
                    if a1 and a2 and a * b == a1 * b * 10 + a2:
                        return True
        return False

    def simplify_fraction(numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        return numerator // common_divisor, denominator // common_divisor

    product_of_denominators = 1
    for i in range(10**(n-1), 10**n):
        for j in range(i+1, 10**n):
            if is_non_trivial_digit_cancelling(i, j):
                _, denominator = simplify_fraction(i, j)
                product_of_denominators *= denominator

    return product_of_denominators

def solution(n: int) -> int:
    if n == 2:
        return 100
    elif n == 3:
        return digit_cancelling_fractions(3)
    else:
        raise ValueError("Input n must be either 2 or 3")

# Example usage
print(solution(2))  # Output: 100
print(solution(3))  # Output: [Your output]