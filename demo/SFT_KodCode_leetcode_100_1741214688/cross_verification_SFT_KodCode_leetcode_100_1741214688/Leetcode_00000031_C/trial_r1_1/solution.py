def find_largest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
    
    max_length = 1
    result = s[0]
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (left + 1, right - 1)
    
    for i in range(len(s)):
        # Odd length palindromes
        start, end = expand_around_center(i, i)
        current_length = end - start + 1
        current_pal = s[start:end+1]
        if current_length > max_length:
            max_length = current_length
            result = current_pal
        elif current_length == max_length:
            if current_pal > result:
                result = current_pal
        
        # Even length palindromes
        if i < len(s) - 1:
            start_e, end_e = expand_around_center(i, i + 1)
            current_length_e = end_e - start_e + 1
            if current_length_e > 0:
                current_pal_e = s[start_e:end_e+1]
                if current_length_e > max_length:
                    max_length = current_length_e
                    result = current_pal_e
                elif current_length_e == max_length:
                    if current_pal_e > result:
                        result = current_pal_e
    
    return result