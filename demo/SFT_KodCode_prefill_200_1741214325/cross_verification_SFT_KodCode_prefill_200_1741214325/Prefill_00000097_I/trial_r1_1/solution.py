def remove_duplicates_preserve_order(input_list):
    seen = {}
    result = []
    for element in input_list:
        if element not in seen:
            seen[element] = True
            result.append(element)
    return result