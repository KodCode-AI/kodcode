def count_substring_occurrences(string, substring):
    """
    Counts the number of times the substring occurs in the given string.
    
    :param string: The main string to search in.
    :param substring: The substring to search for.
    :return: The number of times the substring occurs in the string.
    """
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            break
    return count