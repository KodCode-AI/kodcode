from typing import List

def string_to_ascii_list(input_string: str) -> List[int]:
    return [ord(char) for char in input_string]