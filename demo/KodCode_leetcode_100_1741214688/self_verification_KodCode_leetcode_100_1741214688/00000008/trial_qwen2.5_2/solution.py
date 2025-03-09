def min_swaps_to_target(words, target):
    """
    Returns the minimum number of adjacent swaps required to arrange the strings in words
    to form the target string. If it is not possible to form the target, returns -1.
    """
    word_to_index = {word: idx for idx, word in enumerate(words)}
    target_words = target.split()
    words_pointer = 0
    swaps = 0
    
    for target_word in target_words:
        if target_word not in word_to_index:
            return -1
        index = word_to_index[target_word]
        while index > words_pointer:
            words_pointer += 1
            swaps += 1
        words_pointer = index + 1
    
    return swaps