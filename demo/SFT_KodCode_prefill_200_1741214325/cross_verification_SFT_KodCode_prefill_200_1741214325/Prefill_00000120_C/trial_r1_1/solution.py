def merge_and_sum_dictionaries(dict1, dict2):
    result = dict2.copy()
    for key, value in dict1.items():
        if key in result:
            result[key] += value
    return result