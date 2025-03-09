def find_longest_recurring_cycle(denominator_limit: int) -> int:
    """
    Find the value of d < denominator_limit for which 1/d contains the longest recurring cycle in its decimal fraction part.

    :param denominator_limit: The upper limit for the search (exclusive).
    :return: The value of d that produces the longest recurring cycle.
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    max_cycle_length = 0
    result_d = 0

    for d in range(2, denominator_limit):
        if d % 2 == 0 or d % 5 == 0:
            continue  # Skip even numbers and multiples of 5

        remainder_set = set()
        remainder = 1
        while remainder != 0:
            if remainder in remainder_set:
                cycle_length = len(remainder_set)
                if cycle_length > max_cycle_length:
                    max_cycle_length = cycle_length
                    result_d = d
                break

            remainder_set.add(remainder)
            remainder = (remainder * 10) % d

    return result_d