def find_weird_numbers(numbers):
    """
    Returns a list of weird numbers from the given list of natural numbers.
    A weird number is a number that is abundant but not semiperfect.
    """
    def is_abundant(n):
        divisors_sum = sum([d for d in range(1, n) if n % d == 0])
        return divisors_sum > n

    def is_semiperfect(n):
        divisors = [d for d in range(1, n) if n % d == 0]
        return any(sum(divisors[:i]) == n for i in range(1, len(divisors)+1))

    weird_numbers = []
    for number in numbers:
        if is_abundant(number) and not is_semiperfect(number):
            weird_numbers.append(number)
    return weird_numbers