def merge_and_sum_dictionaries(dict1, dict2):
    all_keys = set(dict1.keys()) | set(dict2.keys())
    merged = {}
    for key in all_keys:
        merged[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return merged