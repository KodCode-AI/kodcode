def is_valid_palindrome(s):
    # Clean the string by including only alphanumeric characters and converting to lowercase
    cleaned = [c.lower() for c in s if c.isalnum()]
    cleaned_str = ''.join(cleaned)
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]