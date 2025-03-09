def count_substring_occurrences(main_string, substring):
    """
    Returns the number of times the substring appears in the main string,
    ignoring case.
    """
    return sum(main_string[i:i+len(substring)].casefold() == substring.casefold() for i in range(len(main_string)))