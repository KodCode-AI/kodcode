def search_word_in_file(file_path, word):
    """
    Searches for a specific word in a text file and returns a list of line numbers
    where the word is found. The search is case-insensitive.
    
    :param file_path: Path to the text file.
    :param word: The word to search for.
    :return: A list of line numbers where the word is found.
    """
    word = word.lower()
    found_lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if word in line.lower():
                found_lines.append(line_number)
    return found_lines