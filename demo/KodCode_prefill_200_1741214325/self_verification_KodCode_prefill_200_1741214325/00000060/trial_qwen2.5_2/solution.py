def filter_strings(list_of_strings, substring):
    """
    Returns a new list containing only the strings from the input list that include the specified substring.
    """
    return [s for s in list_of_strings if substring in s]