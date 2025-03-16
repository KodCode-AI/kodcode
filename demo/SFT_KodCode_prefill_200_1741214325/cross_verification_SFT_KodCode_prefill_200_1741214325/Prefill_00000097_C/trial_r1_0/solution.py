from typing import List, Union, Tuple

def remove_duplicates_preserve_order(lst: List[Union[int, str, Tuple]]) -> List[Union[int, str, Tuple]]:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result