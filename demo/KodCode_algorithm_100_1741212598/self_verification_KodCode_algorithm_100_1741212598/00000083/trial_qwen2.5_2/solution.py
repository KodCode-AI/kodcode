import re

class Card:
    def __init__(self, value):
        self.value = value

class PokerHand:
    CARD_RANKS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, hand):
        self.cards = sorted([self._parse_card(card) for card in re.findall(r'([2-9TJKQA][SDCH])', hand)], key=lambda card: self.CARD_RANKS[card.value], reverse=True)

    def _parse_card(self, card):
        return Card(self.CARD_RANKS[card[0]])

    def _is_flush(self):
        return all(card.suit == self.cards[0].suit for card in self.cards)

    def _is_straight(self):
        values = [card.value for card in self.cards]
        return values == list(range(values[0], values[0] - 5, -1)) or values == [14, 5, 4, 3, 2]

    def _is_five_high_straight(self):
        values = [card.value for card in self.cards]
        return sorted(values) == [10, 11, 12, 13, 14]

    def _count_pairs(self):
        counts = [0] * 15
        for card in self.cards:
            counts[card.value] += 1
        return [value for value, count in enumerate(counts, 2) if count >= 2]

    def _is㿠nhand(self):
        return self._is_five_high_straight()

    def get_hand_type(self):
        if self._is_five_high_straight() and self._is_flush():
            return 'Straight Flush'
        pairs = self._count_pairs()
        if len(pairs) == 2 and pairs[0] - pairs[1] == 2:
            return 'Four of a Kind'
        if len(pairs) == 2:
            return 'Full House'
        if self._is_flush():
            return 'Flush'
        if self._is_straight():
            return 'Straight'
        if len(pairs) == 1:
            return 'Three of a Kind'
        if len(pairs) == 3:
            return 'Two Pair'
        if len(pairs) == 0:
            return 'High Card'
        return 'Two of a Kind'

    def compare_with(self, other):
        hand_a = self.get_hand_type()
        hand_b = other.get_hand_type()
        if hand_a != hand_b:
            return -1 if PokerHand.HAND_RANKS.index(hand_a) > PokerHand.HAND_RANKS.index(hand_b) else 1
        for a, b in zip(self.cards, other.cards):
            if a.value != b.value:
                return -1 if a.value > b.value else 1
        return 0

PokerHand.HAND_RANKS = ['High Card', 'Two of a Kind', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']