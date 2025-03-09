def divisors_sum(n):
    """
    Returns the sum of proper divisors of n.
    """
    divisors = [1]  # 1 is a proper divisor of every natural number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
    return sum(divisors)

def is_weird_number(n):
    """
    Checks if a number is weird, i.e., abundant but not semiperfect.
    """
    if n < 1 or n > 10000:
        return False
    if divisors_sum(n) <= n:
        return False
    for i in range(1, n):
        if sum([j for j in range(1, n) if n % j == 0 and j < i]) + sum([j for j in range(i + 1, n) if n % j == 0]) == n:
            return False
    return True

def find_weird_numbers(numbers):
    """
    Returns a list of weird numbers from the given list of numbers.
    """
    return [n for n in numbers if is_weird_number(n)]