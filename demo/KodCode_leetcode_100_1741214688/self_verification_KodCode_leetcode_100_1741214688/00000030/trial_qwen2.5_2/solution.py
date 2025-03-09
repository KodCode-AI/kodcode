from collections import Counter

def max_racecar_instances(text: str) -> int:
    """
    Returns the maximum number of "racecar" instances that can be formed using characters from text.
    """
    target_counter = Counter("racecar")
    text_counter = Counter(text)
    
    return min(text_counter[char] // target_counter[char] for char in target_counter if char in text_counter)