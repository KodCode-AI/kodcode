from solution import *

import pytest
from solution import PokerHand

def test_parse_card():
    hand = PokerHand('2H 3D 4S 5H 6C')
    assert len(hand.cards) == 5
    assert hand.cards[0].value == 6
    assert hand.cards[1].value == 5

def test_is_flush():
    hand = PokerHand('2H 3H 4H 5H 6H')
    assert hand._is_flush()
    hand = PokerHand('2H 3D 4S 5H 6C')
    assert not hand._is_flush()

def test_is_straight():
    hand = PokerHand('2H 3D 4S 5H 6C')
    assert hand._is_straight()
    hand = PokerHand('2H 3D 5S 6H 7C')
    assert hand._is_straight()
    hand = PokerHand('2H 3D 5S 7H 8C')
    assert hand._is_straight()
    hand = PokerHand('2H 3D 5S 6H 7C')
    assert hand._is_straight()
    hand = PokerHand('AS KH QH JH TH')
    assert hand._is_flush()
    hand = PokerHand('2H 3D 4S 5H 6C')
    assert not hand._is_straight()

def test_is_five_high_straight():
    hand = PokerHand('AH KH QH JH TH')
    assert hand._is_five_high_straight()
    hand = PokerHand('AH KH QH JH 6H')
    assert not hand._is_five_high_straight()

def test_count_pairs():
    hand = PokerHand('2H 2D 4S 5H 6C')
    assert hand._count_pairs() == [2]
    hand = PokerHand('2H 2D 4S 5H 5C')
    assert hand._count_pairs() == [2, 5]
    hand = PokerHand('2H 3D 4S 5H 6C')
    assert hand._count_pairs() == []

def test_get_hand_type():
    hand = PokerHand('2H 2D 4S 5H 6C')
    assert hand.get_hand_type() == 'Two of a Kind'
    hand = PokerHand('2H 2D 4S 4H 6C')
    assert hand.get_hand_type() == 'Two Pair'
    hand = PokerHand('2H 2D 4S 5H 5C')
    assert hand.get_hand_type() == 'Three of a Kind'
    hand = PokerHand('2H 3D 4S 5H 6C')
    assert hand.get_hand_type() == 'Straight'
    hand = PokerHand('2H 3H 4S 5H 6H')
    assert hand.get_hand_type() == 'Flush'
    hand = PokerHand('2H 3H 4H 5H 6H')
    assert hand.get_hand_type() == 'Straight Flush'
    hand = PokerHand('2H 3D 4S 5H 5C')
    assert hand.get_hand_type() == 'Full House'
    hand = PokerHand('2H 2D 4S 4H 6C')
    assert hand.get_hand_type() == 'Two Pair'
    hand = PokerHand('2H 2D 2S 2H 3C')
    assert hand.get_hand_type() == 'Four of a Kind'
    hand = PokerHand('2H 3H 4H 5H 6H')
    assert hand.get_hand_type() == 'Straight Flush'
    hand = PokerHand('2H 3H 4H 5H 6H')
    assert hand.get_hand_type() == 'Straight Flush'

def test_compare_with():
    assert PokerHand('2H 3D 4S 5H 6C').compare_with(PokerHand('2H 3D 4S 5H 6C')) == 0
    assert PokerHand('2H 3D 4S 5H 6C').compare_with(PokerHand('AH 2D 4S 5H 7C')) == 1
    assert PokerHand('AH 2D 4S 5H 7C').compare_with(PokerHand('2H 3D 4S 5H 6C')) == -1
    assert PokerHand('2H 3D 4S 5H 6C').compare_with(PokerHand('2H 2D 4S 5H 6C')) == -1
    assert PokerHand('2H 3D 4S 5H 6C').compare_with(PokerHand('2H 2D 4S 5H 5C')) == -1
    assert PokerHand('2H 3D 4S 5H 6C').compare_with(PokerHand('2H 2D 4S 4H 6C')) == -1