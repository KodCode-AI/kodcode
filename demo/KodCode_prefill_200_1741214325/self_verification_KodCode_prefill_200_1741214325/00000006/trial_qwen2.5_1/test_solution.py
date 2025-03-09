from solution import *

import os
from solution import search_word_in_file

# Assuming there is a test file named 'test.txt' with the following content:
# This is a test file.
# The word test is present in this file.
# Another test line. This is to check for multiple occurrences.

def setup_test_file():
    with open('test.txt', 'w', encoding='utf-8') as file:
        file.write("This is a test file.\n")
        file.write("The word test is present in this file.\n")
        file.write("Another test line. This is to check for multiple occurrences.\n")

def teardown_test_file():
    try:
        os.remove('test.txt')
    except FileNotFoundError:
        pass

def test_search_word_in_file():
    setup_test_file()
    result = search_word_in_file('test.txt', 'test')
    assert result == [2, 3]
    result = search_word_in_file('test.txt', 'file')
    assert result == [1, 2]
    result = search_word_in_file('test.txt', 'notfound')
    assert result == []
    teardown_test_file()

def test_search_word_case_insensitive():
    setup_test_file()
    result = search_word_in_file('test.txt', 'TEST')
    assert result == [2, 3]
    teardown_test_file()