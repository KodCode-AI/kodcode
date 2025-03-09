def count_balanced_substrings(s: str) -> int:
    """
    Returns the number of balanced substrings in the given string s.
    A balanced substring has an equal number of vowels and consonants.
    """
    vowels = 'aeiou'
    balanced_count = 0
    for i in range(len(s)):
        vowel_count, consonant_count = 0, 0
        for j in range(i, len(s)):
            if s[j] in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
            if vowel_count == consonant_count:
                balanced_count += 1
    return balanced_count