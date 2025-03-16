def count_uppercase(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            count += 1
    return count