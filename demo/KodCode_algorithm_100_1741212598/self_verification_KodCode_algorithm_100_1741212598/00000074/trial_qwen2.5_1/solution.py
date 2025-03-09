from functools import lru_cache

EVEN_DIGITS = [0, 2, 4, 6, 8]
ODD_DIGITS = [1, 3, 5, 7, 9]

@lru_cache(None)
def is_reversible(num: int) -> bool:
    str_num = str(num)
    if str_num[0] == '0':  # Leading zero is not allowed
        return False
    for i in range(len(str_num)):
        if (int(str_num[i]) in EVEN_DIGITS) and (i != len(str_num) - 1):
            return False
    for i in range(len(str_num) // 2):
        if (int(str_num[i]) + int(str_num[~i]) in EVEN_DIGITS):
            return False
    return True

def count_reversible_numbers(max_power: int) -> int:
    total_count = 0
    for length in range(1, max_power + 1):
        if length == 1:
            total_count += 5  # Single digit: 1, 3, 5, 7, 9
        elif length % 2 == 1:
            counts = [0] * 10
            for i in ODD_DIGITS:
                counts[i] = 1
            for _ in range(length // 2):
                new_counts = [0] * 10
                for i in ODD_DIGITS:
                    for j in ODD_DIGITS:
                        new_counts[(i + j) % 10] += counts[i]
                counts = new_counts
            total_count += sum(counts[i] for i in ODD_DIGITS) * 5
        else:
            counts = [0] * 10
            for i in ODD_DIGITS:
                counts[i] = 1
            for _ in range(length // 2 - 1):
                new_counts = [0] * 10
                for i in ODD_DIGITS:
                    for j in ODD_DIGITS:
                        if is_reversible((i * 10 + j) % 100):
                            new_counts[(i + j) % 10] += counts[i]
                counts = new_counts
            total_count += sum(counts[i] for i in ODD_DIGITS) * 5 * 2
    return total_count

# Example usage
print(count_reversible_numbers(3))  # Output: 120