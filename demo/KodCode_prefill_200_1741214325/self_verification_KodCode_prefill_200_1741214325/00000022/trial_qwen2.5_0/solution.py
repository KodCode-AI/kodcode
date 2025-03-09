def count_substring(string, substring):
    """
    Returns the number of occurrences of a substring within a given string, case-insensitively.
    
    :param string: The main string where we want to search for occurrences.
    :param substring: The substring we want to count within the main string.
    :return: The count of occurrences of the substring within the string.
    """
    return sum(1 for i in range(len(string)) if string[i:i+len(substring)].lower() == substring.lower())