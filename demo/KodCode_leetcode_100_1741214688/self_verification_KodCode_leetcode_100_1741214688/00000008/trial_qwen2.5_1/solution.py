def min_swaps_to_target(words, target):
    """
    Returns the minimum number of swaps required to arrange the strings
    in 'words' to match the 'target' string. Each string in 'words' can only
    be used once, and the order must match 'target'.
    """
    word_positions = {word: i for i, word in enumerate(target)}
    words = [word for word in words if word in word_positions]
    target = [word for word in target if word in word_positions]
    positions = {word: i for i, word in enumerate(words)}
    swaps = 0

    for i, word in enumerate(target):
        current_position = positions[word]
        target_position = word_positions[word]
        if current_position != target_position:
            words[i], words[current_position] = words[target_position], words[current_position]
            positions[words[i]] = i
            positions[words[current_position]] = current_position
            swaps += 1

    return swaps if words == target else -1