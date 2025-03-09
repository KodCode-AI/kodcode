def count_balanced_substrings(s: str) -> int:
    """
    Returns the number of balanced substrings in the given string `s`.
    A balanced substring has an equal number of vowels and consonants.
    """
    counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    max_balanced_substrings = 0
    current_vowels = 0
    current_consonants = 0

    for char in s:
        if char in counts:
            current_vowels += 1
            counts[char] += 1
        else:
            current_consonants += 1
        
        if current_vowels == current_consonants:
            max_balanced_substrings += 1
            current_vowels, current_consonants = 0, 0

    return max_balanced_substrings