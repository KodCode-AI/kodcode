def is_valid_palindrome(s):
    cleaned = ''.join([c.lower() for c in s if c.isalnum()])
    return cleaned == cleaned[::-1]