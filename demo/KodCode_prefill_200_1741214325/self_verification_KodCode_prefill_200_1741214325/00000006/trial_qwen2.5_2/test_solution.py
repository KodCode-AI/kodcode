from solution import *

import os
from tempfile import NamedTemporaryFile
from solution import search_word_in_file

def test_search_word_in_file():
    # Create a temporary file with some content
    content = """This is a test file.
This file contains multiple lines with the word 'test'.
The word 'test' appears here again.
An unrelated line without the word.
The test is finished."""
    with NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
        temp_file.write(content)
        file_path = temp_file.name

    # Test the function
    assert search_word_in_file(file_path, 'test') == [2, 3, 6]
    assert search_word_in_file(file_path, 'unrelated') == [5]
    assert search_word_in_file(file_path, 'finish') == [7]
    assert search_word_in_file(file_path, 'not_here') == []

    # Clean up the temporary file
    os.remove(file_path)

def test_case_insensitive_search():
    # Create a temporary file with lowercase and mixed case content
    content = "this IS a TeSt FiLe."
    with NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
        temp_file.write(content)
        file_path = temp_file.name

    # Test the function
    assert search_word_in_file(file_path, 'this') == [1]
    assert search_word_in_file(file_path, 'is') == [1]
    assert search_word_in_file(file_path, 'teSt') == [1]
    assert search_word_in_file(file_path, 'file') == [1]

    # Clean up the temporary file
    os.remove(file_path)