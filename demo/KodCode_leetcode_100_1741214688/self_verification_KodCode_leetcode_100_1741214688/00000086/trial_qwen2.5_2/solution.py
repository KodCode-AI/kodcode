def can_beautiful_string(s: str) -> bool:
    """
    Determines if string s can be made beautiful by swapping at most one vowel character.
    A string is considered beautiful if it is a palindrome and contains exactly three distinct characters.
    """
    vowels = set('aeiou')
    distinct_chars = set(s)
    vowel_count = sum(1 for char in s if char in vowels)
    
    if len(distinct_chars) > 3:
        return False
    
    if len(distinct_chars) == 3 and s != s[::-1]:
        return False
    
    if len(distinct_chars) == 2:
        return s == s[::-1]
    
    if len(distinct_chars) == 1:
        return len(s) == s.count(next(iter(distinct_chars))) and s == s[::-1]
    
    # Exactly three distinct characters and palindrome
    if len(distinct_chars) == 3 and s == s[::-1]:
        # Check if any two characters can be swapped to form a palindrome
        for char in vowels:
            if char in distinct_chars:
                temp_chars = list(distinct_chars)
                temp_chars.remove(char)
                for other_char in temp_chars:
                    # Swap and check if palindrome
                    if (s.replace(other_char, char, 1) + s.replace(other_char, char, 1)[1:] == 
                        s.replace(other_char, char, 1) + s.replace(other_char, char, 1)[0]):
                        return True
    return False