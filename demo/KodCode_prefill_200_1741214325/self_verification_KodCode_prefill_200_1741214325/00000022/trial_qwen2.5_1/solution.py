def count_substring_occurrences(string, substring):
    """
    Counts the number of occurrences of a substring within a given string, ignoring case.
    """
    return sum(substring in string[i:].lower() for i in range(len(string)))