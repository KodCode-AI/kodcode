from typing import List, Union

def remove_duplicates(input_list: List[Union[int, str]]) -> List[Union[int, str]]:
    seen = set()
    result = []
    for element in input_list:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result