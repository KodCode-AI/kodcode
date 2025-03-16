import re

def split_string_into_words(s):
    return re.split(r'[,.\s]+', s)