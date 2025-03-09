def count_vowels(s):
    """
    Returns the number of vowels in the string s.
    Vowels are 'a', 'e', 'i', 'o', 'u', both lowercase and uppercase.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)