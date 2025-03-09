def can_arrange_vowels consonants(s: str) -> bool:
    """
    Determines if the string can be rearranged such that every even-indexed character
    is a vowel and every odd-indexed character is a consonant.
    """
    vowels = set("aeiou")
    odd_vowels, even_consonants = 0, 0

    for i, char in enumerate(s):
        if i % 2 == 0:
            if char in vowels:
                odd_vowels += 1
        else:
            if char not in vowels:
                even_consonants += 1

    return odd_vowels == len(s[1::2]) and even_consonants == len(s[::2]) % 2