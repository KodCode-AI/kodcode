def max_balanced_substring_length(s, k):
    """
    Given a binary string s and an integer k, returns the maximum possible length of a balanced substring.
    A balanced substring has an equal number of 0s and 1s, and k flips are allowed.
    """
    balance = 0
    max_length = 0
    for i in range(len(s)):
        balance += 1 if s[i] == '1' else -1
        if balance < 0:
            balance = 0
        max_length = max(max_length, balance)
    balance = 0
    for i in range(len(s)):
        balance += 1 if s[i] == '0' else -1
        if balance < 0:
            balance = 0
        max_length = max(max_length, balance)
    return min(max_length + k * 2, len(s))