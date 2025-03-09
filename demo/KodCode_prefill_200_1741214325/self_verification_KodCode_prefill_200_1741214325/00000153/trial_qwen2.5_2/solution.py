def count_vowels(s: str) -> int:
    """
    Returns the number of vowels in the string s.
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count