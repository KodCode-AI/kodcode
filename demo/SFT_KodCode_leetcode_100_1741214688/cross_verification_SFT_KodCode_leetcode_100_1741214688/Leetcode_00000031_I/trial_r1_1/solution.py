def largest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    max_length = 0
    candidates = []
    
    # Check odd-length palindromes
    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        start = l + 1
        end = r - 1
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            candidates = [(start, end)]
        elif current_length == max_length:
            candidates.append((start, end))
    
    # Check even-length palindromes
    for i in range(n - 1):
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        start = l + 1
        end = r - 1
        current_length = end - start + 1
        if current_length > max_length:
            max_length = current_length
            candidates = [(start, end)]
        elif current_length == max_length:
            candidates.append((start, end))
    
    # Determine the lexicographically largest substring
    max_sub = None
    for (start, end) in candidates:
        current = s[start:end+1]
        if max_sub is None or current > max_sub:
            max_sub = current
    
    # In case no palindromes found (only possible if the string is empty, but handled earlier)
    return max_sub if max_sub is not None else s[0] if n > 0 else ""