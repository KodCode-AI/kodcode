from typing import List, Union, Tuple

def remove_duplicates_preserve_order(lst: List[Union[int, str, Tuple]]) -> List[Union[int, str, Tuple]]:
    seen = set()
    seen_list = []
    for element in lst:
        if element not in seen:
            seen.add(element)
            seen_list.append(element)
    return seen_list