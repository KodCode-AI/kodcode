def is_valid_palindrome(s):
    # Filter and normalize the string
    processed = [char.lower() for char in s if char.isalnum()]
    # Join the characters into a string
    processed_str = ''.join(processed)
    # Check if the string is a palindrome
    return processed_str == processed_str[::-1]