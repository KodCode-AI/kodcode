from collections import Counter

def max_racecar_instances(text: str) -> int:
    """
    Given a string `text`, returns the maximum number of "racecar" instances that can be formed using the characters in `text`.
    Each character in `text` can be used at most once.
    """
    racecar_counter = Counter("racecar")
    text_counter = Counter(text)
    
    # Calculate the minimum required full matches of "racecar" in text
    return min(text_counter[char] // racecar_counter[char] for char in racecar_counter)