def longest_balanced_substring(s: str) -> int:
    """
    Finds the length of the longest balanced substring.
    A balanced substring has an equal count for each character.
    """
    max_length = 0
    n = len(s)
    
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_balanced(substring):
                max_length = max(max_length, len(substring))
                
    return max_length

def is_balanced(s: str) -> bool:
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    counts = set(char_counts.values())
    return len(counts) == 1