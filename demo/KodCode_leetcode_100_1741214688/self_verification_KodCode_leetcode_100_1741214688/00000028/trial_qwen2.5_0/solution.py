def min_swaps_to_group_ones(s: str) -> int:
    """
    Given a binary string s, returns the minimum number of swaps 
    needed to group all 1s into a contiguous substring.
    """
    ones = [i for i, bit in enumerate(s) if bit == '1']
    n_ones = len(ones)
    if n_ones <= 1:
        return 0

    max_inclusive_ones = 1
    for i in range(n_ones - 1):
        max_inclusive_ones = max(max_inclusive_ones, ones[i + 1] - ones[i])

    return (n_ones - max_inclusive_ones) // 2