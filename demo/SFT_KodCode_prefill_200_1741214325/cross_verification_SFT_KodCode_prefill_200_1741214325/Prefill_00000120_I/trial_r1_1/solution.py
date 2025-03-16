def merge_and_sum_dictionaries(dict1, dict2):
    merged_dict = {}
    # Add all items from the first dictionary
    for key, value in dict1.items():
        merged_dict[key] = value
    # Process items from the second dictionary
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict