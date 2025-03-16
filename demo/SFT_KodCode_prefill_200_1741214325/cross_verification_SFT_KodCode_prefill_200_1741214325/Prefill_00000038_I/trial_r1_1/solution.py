from collections import Counter

def char_frequency(input_string):
    return dict(Counter(input_string))

# Example usage:
string = "hello world"
print(count_character_frequency(string))