def is_palindrome_number(n):
    # Convert the number to a string and reverse it
    reversed_num = str(n)[::-1]
    # Remove any non-digit characters in case of negative numbers
    cleaned_num = str(n).lstrip('-')
    cleaned_reversed = reversed_num.lstrip('-')
    
    # Compare the cleaned numbers
    return cleaned_num == cleaned_reversed