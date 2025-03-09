def can_make_beautiful_palindrome(s: str) -> bool:
    """
    Determine if the string can be modified to be a palindrome with exactly 
    three distinct characters by swapping two vowels.
    """
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    char_counts = [0] * 26  # To count occurrences of each character in the alphabet
    vowel_count = 0
    first_vowel = None
    middle_char = None

    for char in s:
        index = ord(char) - ord('a')
        char_counts[index] += 1

        if char in vowel_set:
            vowel_count += 1
            if first_vowel is None:
                first_vowel = char
            elif char != first_vowel:
                middle_char = char

    # Conditions for a string to be beautiful:
    # 1. At most one character can have an odd count.
    # 2. There should be at most three distinct characters.
    # 3. If there are exactly three distinct characters, one of them must be repeated (palindrome requirement).

    if len(set(s)) > 3:
        return False

    if len(set(s)) < 3:
        return True  # Can always form a palindrome with 1 or 2 distinct characters.

    odd_count_chars = sum(1 for count in char_counts if count % 2 != 0)

    if odd_count_chars > 1:
        return False  # More than one character with an odd count cannot form a palindrome.

    if vowel_count == 3 and all(count == 0 for index in range(26) if char_counts[index] % 2 != 0 and index != ord(first_vowel) - ord('a') and index != ord(middle_char) - ord('a')):
        return False  # Cannot form a palindrome if there are three distinct vowels.

    return True