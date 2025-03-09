def min_swaps_to_group_ones(s: str) -> int:
    """
    Returns the minimum number of swaps required to group all '1's into a contiguous substring.
    """
    ones_count = s.count('1')
    max_ones_in_window = 0
    current_ones = 0
    for i in range(len(s)):
        if s[i] == '1':
            current_ones += 1
        if i >= ones_count and s[i - ones_count] == '1':
            current_ones -= 1
        max_ones_in_window = max(max_ones_in_window, current_ones)
    # The minimum swaps required is the number of '1's in the string minus the maximum count of '1's in any window.
    return ones_count - max_ones_in_window