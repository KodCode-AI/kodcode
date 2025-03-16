from typing import List, Union

def remove_duplicates(input_list: List[Union[int, str]]) -> List[Union[int, str]]:
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result