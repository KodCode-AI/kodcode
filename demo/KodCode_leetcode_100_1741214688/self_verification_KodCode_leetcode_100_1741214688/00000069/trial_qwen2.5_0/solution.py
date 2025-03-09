def can_rearrange_string(s: str) -> bool:
    """
    Determines if the string can be rearranged such that every even-indexed
    character is a vowel and every odd-indexed character is a consonant.
    """
    vowels = set('aeiou')
    # Count number of vowels and consonants in the even and odd positions
    even_vowels = sum(1 for i in range(0, len(s), 2) if s[i] in vowels)
    odd_consonants = sum(1 for i in range(1, len(s), 2) if s[i] not in vowels)
    return even_vowels == (len(s) + 1) // 2 and odd_consonants == len(s) // 2