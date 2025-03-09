def make_smallest_palindrome(s: str, k: int) -> str:
    """
    Generates the lexicographically smallest palindrome by swapping adjacent characters at most k times.
    If impossible, returns an empty string.
    """
    if k >= len(s) // 2:
        return s
    
    s_list = list(s)
    n = len(s)
    cnt = 0
    
    for i in range(n // 2):
        if s_list[i] != s_list[n - i - 1]:
            for j in range(n - i - 1):
                if s_list[i + j + 1] == s_list[n - i - 1]:
                    s_list[i + j + 1], s_list[n - i - 1] = s_list[n - i - 1], s_list[i + j + 1]
                    cnt += j + 1
                    break
            else:
                for j in range(n - i - 1):
                    if s_list[n - j - 1] == s_list[i]:
                        s_list[i], s_list[n - j - 1] = s_list[n - j - 1], s_list[i]
                        cnt += j + 1
                        break
            if cnt > k:
                return ""
            k -= cnt
            cnt = 0
    return ''.join(s_list)