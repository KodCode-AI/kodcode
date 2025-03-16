import re

def split_string_into_words(s):
    words = re.split(r'[,. ]+', s)
    return [word for word in words if word]