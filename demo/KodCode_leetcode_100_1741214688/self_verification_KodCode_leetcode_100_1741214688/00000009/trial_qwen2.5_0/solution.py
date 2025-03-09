def max_balanced_substring_length(s, k):
    """
    Given a string s and an integer k, returns the length of the longest balanced
    substring. A substring is balanced if the frequency of each letter is at most k.
    """
    from collections import defaultdict
    
    char_count = defaultdict(int)
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        while min(char_count.values()) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length