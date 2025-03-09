def max_racecar_instances(text):
    """
    Returns the maximum number of "racecar" instances that can be formed from the given text.
    """
    from collections import Counter
    
    required_chars = Counter("racecar")
    text_counter = Counter(text)
    min_instances = float('inf')
    
    for char in required_chars:
        if char in text_counter:
            min_instances = min(min_instances, text_counter[char] // required_chars[char])
        else:
            return 0
    
    return min_instances