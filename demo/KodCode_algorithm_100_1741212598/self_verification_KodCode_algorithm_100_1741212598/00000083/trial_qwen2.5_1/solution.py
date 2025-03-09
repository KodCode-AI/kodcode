class PokerHand:
    def __init__(self, hand):
        """
        Initializes a PokerHand object with a given hand string.
        The hand string is expected to be in the format '2H 3D TD KC AS', where
        AH represents an Ace of Hearts, 2H represents a 2 of Hearts, etc.
        """
        self.hand = hand
        self.cards = sorted([card[:-1] for card in hand.split()])
        self.ranks = sorted([int(card[:-1]) if card[:-1].isdigit() else 14 for card in hand.split()])

    def is_flush(self):
        """
        Checks if the hand is a flush.
        """
        suits = [card[-1] for card in self.hand.split()]
        return len(set(suits)) == 1

    def is_straight(self):
        """
        Checks if the hand is a straight.
        """
        card_values = [5, 4, 3, 2, 1] + list(range(6, 15))
        return all(self.ranks[i] == self.ranks[i-1] + 1 for i in range(4)) or self._is_five_high_straight()

    def _is_five_high_straight(self):
        """
        Checks if the hand is a 5-high straight (ace, 2, 3, 4, 5).
        """
        return all(self.ranks[i] in [9, 10, 11, 12, 13] for i in range(4)) and self.ranks[-1] == 14

    def count_pairs(self):
        """
        Counts the number of pairs in the hand.
        """
        pairs = sum(self.ranks[i] == self.ranks[i+1] for i in range(4))
        return pairs

    def hand_type(self):
        """
        Determines the type of the poker hand based on the given rules.
        """
        if self.is_flush() and self.is_straight():
            return 'Royal Flush'
        if self.is_straight() and self.ranks[0] == 10:
            return 'Straight Flush'
        if self.is_flush():
            return 'Flush'
        if self.is_straight():
            return 'Straight'
        pairs = self.count_pairs()
        if pairs == 4:
            return 'Four of a Kind'
        if pairs == 3:
            return 'Full House'
        if self.is_flush():
            return 'Flush'
        if self.is_straight():
            return 'Straight'
        return 'High Card'

    def compare_with(self, other):
        """
        Compares the hand with another hand and returns -1, 0, or 1 based on the comparison.
        """
        hand_type = self.hand_type()
        other_type = other.hand_type()
        if hand_type == other_type:
            self_ranks = sorted([self.ranks[4-i*2] for i in range(5)])
            other_ranks = sorted([other.ranks[4-i*2] for i in range(5)])
            for r, other_r in zip(self_ranks, other_ranks):
                if r > other_r:
                    return 1
                elif r < other_r:
                    return -1
            return 0
        hand_types = ['High Card', 'Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']
        return 1 if hand_types.index(hand_type) > hand_types.index(other_type) else -1