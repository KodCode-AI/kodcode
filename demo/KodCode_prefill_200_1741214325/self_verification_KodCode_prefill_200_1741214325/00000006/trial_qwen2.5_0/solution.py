def search_word_in_file(file_path, search_word):
    """
    Searches for a specific word in a text file and returns a list of line numbers where the word is found.
    Ignores case sensitivity.
    """
    result = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if search_word.lower() in line.lower():
                    result.append(line_number)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    return result