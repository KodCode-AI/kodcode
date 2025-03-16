def is_palindrome_number(number: int) -> bool:
    if number < 0:
        return False
    original = number
    reversed_num = 0
    while number > 0:
        remainder = number % 10
        reversed_num = reversed_num * 10 + remainder
        number = number // 10
    return original == reversed_num