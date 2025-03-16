def remove_duplicates_preserve_order(input_list):
    unique_list = []
    seen = set()
    for element in input_list:
        if element not in seen:
            unique_list.append(element)
            seen.add(element)
    return unique_list