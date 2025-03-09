def count_substring_occurrences(main_string, substring):
    """
    Returns the number of times the substring occurs in the main string.
    """
    count = start = 0
    while True:
        start = main_string.find(substring, start) + 1
        if start > 0:
            count += 1
        else:
            break
    return count