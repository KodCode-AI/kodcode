from solution import *

def test_search_word_in_file():
    import os

    # Create a temporary file with some content
    test_file_path = 'test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as file:
        file.write("This is a test. This is only a test.\n")
        file.write("Use a test for testing purposes.\n")
        file.write("Testing is a common practice.\n")
        file.write("This test is for testing functions.\n")

    assert search_word_in_file(test_file_path, 'test') == [1, 2, 3, 4]
    assert search_word_in_file(test_file_path, 'common') == [3]
    assert search_word_in_file(test_file_path, 'notfound') == []
    assert search_word_in_file(test_file_path, 'this') == [1, 2, 4]
    assert search_word_in_file(test_file_path, 'use') == [2]

    # Clean up
    os.remove(test_file_path)

def test_search_word_case_insensitivity():
    test_file_path = 'test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as file:
        file.write("WORD is here, but not in capital letters.\n")
        file.write("word is here, in lowercase.\n")

    assert search_word_in_file(test_file_path, 'word') == [1, 2]
    os.remove(test_file_path)

def test_file_not_found():
    assert search_word_in_file('nonexistentfile.txt', 'anyword') == []