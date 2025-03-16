def length_of_longest_substring(s):
    if not s:
        return ""
    
    max_length = 0
    start_idx = 0
    current_start = 0
    last_seen = {}
    
    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= current_start:
            current_start = last_seen[char] + 1
        last_seen[char] = i
        
        current_length = i - current_start + 1
        if current_length > max_length:
            max_length = current_length
            start_idx = current_start
    
    return s[start_idx : start_idx + max_length]