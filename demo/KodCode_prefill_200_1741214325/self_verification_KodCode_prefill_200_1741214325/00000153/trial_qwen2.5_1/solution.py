def count_vowels(input_string):
    """
    Returns the number of vowels in the input string. The function considers 'a', 'e', 'i', 'o', 'u',
    both in lowercase and uppercase.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_string if char in vowels)