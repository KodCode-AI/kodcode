from typing import List, Tuple

def sort_tuples(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return sorted(lst, key=lambda x: (x[1], x[0]))