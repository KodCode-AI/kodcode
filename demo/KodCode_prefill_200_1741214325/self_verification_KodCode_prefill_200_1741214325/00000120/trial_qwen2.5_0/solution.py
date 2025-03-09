def merge_and_sum_dicts(dict1, dict2):
    """
    Merges two dictionaries. If a key is present in both, sums their values.
    If a key is only present in one dictionary, its value is taken as is.
    """
    # Sum the values of keys that are present in both dictionaries
    for key in dict2:
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1