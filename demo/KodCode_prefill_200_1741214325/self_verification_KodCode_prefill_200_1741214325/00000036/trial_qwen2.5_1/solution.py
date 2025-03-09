To write a Python function that prints all prime numbers in a given range, follow these steps:
1. Define the function with start and end parameters that define the range.
2. Iterate through each number in the range.
3. For each number, check if it is a prime number.
4. Print or return the prime numbers as needed.

### Factors to consider:
- **Efficiency:** Check for prime numbers as efficiently as possible.
- **Edge Cases:** Handle ranges that could include negative numbers, zero, or even large numbers.
- **Optimization:** Use the smallest possible divisors to check for primality (up to the square root of the number).

def is_prime(num):
    """Returns True if num is a prime number, else False."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime_numbers(start, end):
    """Prints all the prime numbers in the given range."""
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            print(num)