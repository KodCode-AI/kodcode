def find_longest_recurring_cycle(denominator_limit: int) -> int:
    """
    Find the value of d < denominator_limit for which 1/d contains the longest recurring cycle in its decimal fraction part.

    :param denominator_limit: The upper limit for the search (exclusive).
    :return: The value of d that produces the longest recurring cycle.
    """
    max_length = 0
    result_d = 1

    for d in range(2, denominator_limit):
        remainder_set = set()
        remainder = 1
        while remainder != 0:
            if remainder in remainder_set:
                break
            remainder_set.add(remainder)
            remainder = (remainder * 10) % d
            if remainder == 0:
                break
            cycle_length = len(remainder_set)
            if cycle_length > max_length:
                max_length = cycle_length
                result_d = d

    return result_d