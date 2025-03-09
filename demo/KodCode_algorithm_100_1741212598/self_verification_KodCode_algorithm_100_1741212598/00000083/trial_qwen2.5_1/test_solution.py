from solution import *

import pytest

def test_poker_hand_init():
    hand = PokerHand('2H 3D TD KC AS')
    assert hand.cards == ['2', '3', 'T', 'K', 'A']
    assert hand.ranks == [2, 3, 10, 13, 14]

def test_is_flush():
    assert PokerHand('2H 3H TH KH AH').is_flush()
    assert not PokerHand('2H 3D TD KC AS').is_flush()

def test_is_straight():
    assert PokerHand('2H 3D TH KD AC').is_straight()
    assert not PokerHand('2H 3D TD KC AS').is_straight()

def test_is_five_high_straight():
    assert PokerHand('AS 2S 3S 4S 5S')._is_five_high_straight()
    assert not PokerHand('2H 3D TH KD AC')._is_five_high_straight()

def test_count_pairs():
    hand = PokerHand('2H 2D TH KD AC')
    assert hand.count_pairs() == 2

def test_hand_type_royal_flush():
    assert PokerHand('10H JH QH KH AH').hand_type() == 'Royal Flush'

def test_hand_type_straight_flush():
    assert PokerHand('2H 3H TH KH AH').hand_type() == 'Straight Flush'

def test_hand_type_four_of_a_kind():
    assert PokerHand('2H 2D 2S 2C KH').hand_type() == 'Four of a Kind'

def test_hand_type_full_house():
    assert PokerHand('2H 2D TD TH AC').hand_type() == 'Full House'

def test_hand_type_straight():
    assert PokerHand('2H 3D TH KD AC').hand_type() == 'Straight'

def test_hand_type_flush():
    assert PokerHand('2H 3H TH KH AH').hand_type() == 'Flush'

def test_hand_type_high_card():
    assert PokerHand('2H 3D TH KD AC').hand_type() == 'High Card'