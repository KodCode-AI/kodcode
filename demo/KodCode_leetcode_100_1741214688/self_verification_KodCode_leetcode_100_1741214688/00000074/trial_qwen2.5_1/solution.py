def form_smallest_palindrome(s: str) -> str:
    """
    Returns the lexicographically smallest palindrome by swapping any two adjacent characters in the string at most once.
    If it's not possible to form a palindrome by swapping at most one pair of adjacent characters, returns the original string.
    """
    s_list = list(s)
    n = len(s)

    # Find the first mismatch from the start and end
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            j = n - 1 - i
            while i < j and s[i] != s[j]:
                j -= 1

            # If the mismatch is at the boundary, swap the mismatch with the character from the end
            if i == j:
                s_list[i], s_list[n - 1 - i] = s_list[n - 1 - i], s_list[i]

            # Check if the found character can form a palindrome
            while j + 1 < n - 1 - i and s[j + 1] == s[n - 2 - i]:
                j += 1

            if j + 1 < n - 1 - i:
                s_list[j + 1], s_list[n - 1 - i] = s_list[n - 1 - i], s_list[j + 1]

            break

    return ''.join(s_list)