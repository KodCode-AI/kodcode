def filter_strings_by_substring(string_list, substring):
    """
    Filters out strings from the given list that contain the specified substring.

    :param string_list: List of strings to be filtered.
    :param substring: Substring to search for within the strings.
    :return: A list containing only strings that do not contain the specified substring.
    """
    return [s for s in string_list if substring not in s]