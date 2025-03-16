import re
from typing import List

def split_string_into_words(s: str) -> List[str]:
    words = re.split(r'[,. ]+', s)
    return [word for word in words if word]