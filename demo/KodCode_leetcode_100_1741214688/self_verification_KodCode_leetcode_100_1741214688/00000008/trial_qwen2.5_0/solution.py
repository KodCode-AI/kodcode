def min_swaps_to_target(words, target):
    """
    Returns the minimum number of adjacent swaps required to arrange
    the strings in `words` to form the `target` string. If it's not possible, returns -1.
    """
    from collections import defaultdict
    
    # Record positions of each character in the target string
    target_positions = defaultdict(list)
    for idx, char in enumerate(target):
        target_positions[char].append(idx)
    
    # Find positions of the words in the target string
    word_positions = []
    for word in words:
        pos = [target_positions[char].pop(0) for char in word]
        word_positions.append(pos)
    
    # Calculate the minimum swaps if the relative order matches the target
    min_swaps = 0
    for pos in word_positions:
        required_pos = [target_positions[char].pop(0) for char in words[words.index(pos[0])]]
        min_swaps += sum(b - a for a, b in zip(pos, required_pos))
    
    # Check if it's possible to achieve the target order
    if all(len(target_positions[char]) == 0 for char in set(target)):
        return min_swaps // len(word_positions[0])
    else:
        return -1