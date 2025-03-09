def search_word_in_file(file_path, word):
    """
    Searches for a specific word in a text file and returns a list of line numbers
    where the word is found. Ignores case sensitivity.
    
    Parameters:
    file_path (str): Path to the text file.
    word (str): The word to search for.
    
    Returns:
    list: A list of line numbers where the word is found.
    """
    word = word.lower()
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_numbers = []
        for i, line in enumerate(lines, 1):
            if word in line.lower():
                line_numbers.append(i)
        return line_numbers