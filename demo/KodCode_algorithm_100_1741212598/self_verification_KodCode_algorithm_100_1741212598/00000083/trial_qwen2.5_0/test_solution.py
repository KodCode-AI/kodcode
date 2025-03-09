from solution import *

import pytest

@pytest.fixture
def poker_hand():
    return PokerHand

def test_init(poker_hand):
    hand = poker_hand('2D 3D 4D 5D 6D')
    assert hand.hand == ['2', '3', '4', '5', '6']
    assert hand.get_hand_type() == 'flush'

def test_flush(poker_hand):
    hand = poker_hand('2D 3D 4D 5D 6D')
    assert hand._is_flush()
    hand = poker_hand('2S 3H 4C 5D 6H')
    assert not hand._is_flush()

def test_straight(poker_hand):
    hand = poker_hand('2D 3D 4D 5D 6D')
    assert hand._is_straight()
    hand = poker_hand('2S 3H 4C 5D 7H')
    assert not hand._is_straight()

def test_five_high_straight(poker_hand):
    hand = poker_hand('AC 2C 3C 4C 5C')
    assert hand._is_five_high_straight()
    hand = poker_hand('2C 3C 4C 5C 6H')
    assert not hand._is_five_high_straight()

def test_pairs(poker_hand):
    hand = poker_hand('2D 3D 4D JD JD')
    assert hand._count_pairs() == 2
    hand = poker_hand('2D 3D 4D JD QD')
    assert hand._count_pairs() == 0

def test_straight_flush(poker_hand):
    hand = poker_hand('2D 3D 4D 5D 6D')
    assert hand._is_straight_flush()
    hand = poker_hand('2D 3H 4D 5D 6D')
    assert not hand._is_straight_flush()

def test_get_hand_type(poker_hand):
    hand = poker_hand('2D 3D 4D 5D 6D')
    assert hand.get_hand_type() == 'flush'
    hand = poker_hand('2D 3D 4D 5D JD')
    assert hand.get_hand_type() == 'straight'

def test_compare_with(poker_hand):
    hand1 = poker_hand('2D 3D 4D 5D 6H')
    hand2 = poker_hand('3D 4D 5D JD QD')
    assert hand2.compare_with(hand1)

def test_get_count(poker_hand):
    hand = poker_hand('2D 3D 4D 5D JD')
    assert hand.get_count('pair') == 0
    hand = poker_hand('2D 3D 4D JD JD')
    assert hand.get_count('pair') == 2