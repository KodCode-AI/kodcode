def count_substring(string, substring):
    """
    Counts the occurrences of a substring within a given string.
    
    Args:
    string (str): The string to search within.
    substring (str): The substring to count occurrences of.
    
    Returns:
    int: The number of times the substring occurs in the string.
    """
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            return count