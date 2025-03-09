def find_proper_divisors(n):
    """Return a list of proper divisors of n."""
    divisors = [1]  # 1 is a proper divisor of every natural number
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                divisors.append(n // i)
    return divisors

def is_abundant(n):
    """Return True if n is an abundant number."""
    return sum(find_proper_divisors(n)) > n

def is_semiperfect(n):
    """Return True if n is a semiperfect number."""
    divisors = find_proper_divisors(n)
    for i in range(1, 1 << len(divisors)):
        if sum(divisors[j] for j in range(len(divisors)) if (i & (1 << j))) == n:
            return True
    return False

def find_weird_numbers(numbers):
    """Return a list of weird numbers from the input list."""
    return [n for n in numbers if is_abundant(n) and not is_semiperfect(n)]