def find_longest_recurring_cycle(denominator_limit: int) -> int:
    """
    Find the value of d < denominator_limit for which 1/d contains the longest recurring cycle in its decimal fraction part.

    :param denominator_limit: The upper limit for the search (exclusive).
    :return: The value of d that produces the longest recurring cycle.
    """
    longest_cycle = 0
    result_d = 0

    for d in range(2, denominator_limit):
        cycle_length = 0
        remainder = 1
        remainders_seen = {}

        while remainder != 0:
            if remainder in remainders_seen:
                cycle_length = len(remainders_seen) - remainders_seen[remainder]
                break
            remainders_seen[remainder] = len(remainders_seen)
            remainder = (remainder * 10) % d
            cycle_length += 1

        if cycle_length > longest_cycle:
            longest_cycle = cycle_length
            result_d = d

    return result_d