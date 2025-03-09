def count_substrings(words, target):
    """
    Returns the number of strings in words that contain the target as a substring.
    """
    return sum(target in word for word in words)