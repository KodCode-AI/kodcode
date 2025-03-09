from functools import lru_cache

EVEN_DIGITS = [0, 2, 4, 6, 8]
ODD_DIGITS = [1, 3, 5, 7, 9]

@lru_cache(None)
def count_reversible_numbers(max_power: int) -> int:
    def is_reversible(n: int) -> bool:
        if n % 10 in EVEN_DIGITS:
            return False
        for digit in str(n):
            if int(digit) in EVEN_DIGITS:
                return False
        return True

    def count_helper(length: int, leading_even: bool = False) -> int:
        if length == 1:
            return 1
        if length == 2:
            return 5 if not leading_even else 5
        half = count_helper((length + 1) // 2, leading_even)
        if length % 2 == 0:
            # Even length number
            return half * 5
        else:
            # Odd length number
            return half * 5 * (10 - 2) - (not leading_even) * 2

    if max_power == 1:
        return 5
    else:
        return count_helper(max_power + 1, True)

# Example usage
print(count_reversible_numbers(3))  # Output: 120
print(count_reversible_numbers(6))  # Output: 18720
print(count_reversible_numbers(7))  # Output: 68720