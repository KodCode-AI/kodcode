from typing import List, Union, Tuple

def remove_duplicates_preserve_order(lst: List[Union[int, str, Tuple]]) -> List[Union[int, str, Tuple]]:
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result