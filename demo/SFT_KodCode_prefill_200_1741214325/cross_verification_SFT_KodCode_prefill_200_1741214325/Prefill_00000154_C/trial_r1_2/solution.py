import re
from typing import List

def split_string_into_words(s: str) -> List[str]:
    pattern = r'[, .]+'
    parts = re.split(pattern, s)
    return [part for part in parts if part]