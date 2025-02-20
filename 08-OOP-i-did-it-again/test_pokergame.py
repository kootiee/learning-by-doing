from pokergame import Pokergame
from pokerhand import Pokerhand


def test_get_hand_royal_flush_and_straight_flush():
    hand = Pokergame(
        Pokerhand(['AS', '10S', 'JS', 'QS', 'KS']),
        Pokerhand(['AS', '2S', '3S', '4S', '5S'])
    )
    assert hand.compare_hands() == (
        ['player 1', 'royal flush'], ['player 2', 'straight flush'])


def test_get_hand_full_house_and_flush():
    hand = Pokergame(
        Pokerhand(['2H', '2D', '2S', '5C', '5H']),
        Pokerhand(['AS', 'KS', 'QS', 'JS', '10S'])
    )
    assert hand.compare_hands() == (
        ['player 2', 'royal flush'], ['player 1', 'full house'])



def test_get_hand_four_of_a_kind_and_three_of_a_kind():
    hand = Pokergame(
        Pokerhand(['8H', '8D', '8S', '8C', '3D']),
        Pokerhand(['6H', '6D', '6S', '3C', '3H'])
    )
    assert hand.compare_hands() == (
        ['player 1', 'four of a kind'], ['player 2', 'full house'])


def test_get_hand_straight_and_high_card():
    hand = Pokergame(
        Pokerhand(['3D', '4S', '5C', '6H', '7D']),
        Pokerhand(['KS', '8D', '6C', '3S', '2H'])
    )
    assert hand.compare_hands() == (
        ['player 1', 'straight'], ['player 2', 'high card'])


def test_get_hand_two_pair_and_one_pair():
    hand = Pokergame(
        Pokerhand(['3H', '3D', '6S', '6C', 'KH']),
        Pokerhand(['4S', '4D', '10H', '5C', '9S'])
    )
    assert hand.compare_hands() == (
        ['player 1', 'two pair'], ['player 2', 'one pair'])


def test_get_hand_flush_and_high_card():
    hand = Pokergame(
        Pokerhand(['2H', '4H', '7H', '10H', 'KH']),
        Pokerhand(['8D', '3C', '5S', '6D', '9H'])
    )
    assert hand.compare_hands() == (
        ['player 1', 'flush'], ['player 2', 'high card'])
