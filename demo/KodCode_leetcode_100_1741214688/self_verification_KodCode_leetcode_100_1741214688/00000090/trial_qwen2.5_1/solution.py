def count_balanced_substrings(s):
    """
    Counts the number of balanced substrings in the given string `s`.
    A balanced substring has an equal number of vowels and consonants.
    """
    vowels = set('aeiou')
    count, balanced_count = 0, 0
    
    for char in s:
        if char in vowels:
            count += 1
        else:
            count -= 1
        
        if count == 0:
            balanced_count += 1
    
    return balanced_count