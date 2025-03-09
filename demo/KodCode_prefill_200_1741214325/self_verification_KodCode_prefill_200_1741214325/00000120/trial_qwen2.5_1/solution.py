def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries. If the same key exists in both dictionaries,
    their values will be summed up. If not, the value from the second dictionary
    will simply be added to the result.
    """
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict