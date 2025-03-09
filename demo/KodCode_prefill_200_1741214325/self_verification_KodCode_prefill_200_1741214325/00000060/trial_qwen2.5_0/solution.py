def filter_strings_with_substring(string_list, substring):
    """
    Returns a list of strings from the input list that contain the specified substring.
    
    :param string_list: List of strings to be filtered
    :param substring: Substring to filter the strings by
    :return: List of strings containing the specified substring
    """
    return [s for s in string_list if substring in s]