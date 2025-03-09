def merge_and_sum_dictionaries(dict1, dict2):
    """
    Merges two dictionaries. If the same key exists in both, sums their values. 
    If not, from the second dictionary, the value should be added to the result.
    """
    result = {**dict1}  # Start with the first dictionary's keys and values
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value  # Sum or add the new value
    return result