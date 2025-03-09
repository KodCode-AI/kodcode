def max_balanced_substring_length(s: str, k: int) -> int:
    """
    Returns the maximum possible length of a balanced substring of s
    after flipping at most k characters. A balanced substring has an
    equal number of '0's and '1's.
    """
    max_length = 0
    # Convert the string into -1 for '0' and 1 for '1' to track balance.
    s = [1 if char == '1' else -1 for char in s]
    sum_prefix, len_prefix = 0, 0
    # Record the first occurrence of each prefix sum.
    seen = {0: -1}
    for i, num in enumerate(s):
        sum_prefix += num
        # Record the first occurrence of this prefix sum.
        if sum_prefix not in seen:
            seen[sum_prefix] = i
        # If the current length minus the length at the first occurrence
        # of the current prefix sum is <= k, it means we can balance.
        if sum_prefix in seen and (i - seen[sum_prefix] <= k + 1):
            max_length = max(max_length, i - seen[sum_prefix])
        # If the prefix sum + k can form a balanced substring, update max_length.
        if sum_prefix + k in seen and (i - seen[sum_prefix + k] <= k + 1):
            max_length = max(max_length, i - seen[sum_prefix + k])
    return max_length