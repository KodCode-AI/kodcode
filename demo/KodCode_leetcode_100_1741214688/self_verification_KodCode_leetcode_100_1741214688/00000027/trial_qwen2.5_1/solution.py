def count_substring_occurrences(words, target):
    """
    Returns the number of strings in 'words' that contain 'target' as a substring.
    """
    return sum(target in word for word in words)