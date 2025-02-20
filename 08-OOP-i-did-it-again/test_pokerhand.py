from pokerhand import Pokerhand


def test_is_valid_hand_():
    hand = Pokerhand(['3S', 'JH', '6D', '4D', 'AD'])
    assert hand.is_valid_hand()


def test_is_valid_hand_less_than_5_cards():
    hand = Pokerhand(['4D', 'JH', '8S', 'AS'])
    assert not hand.is_valid_hand()


def test_is_valid_hand_more_than_5_cards():
    hand = Pokerhand(['2S', 'KH', '6S', '4S', '10D', 'AH'])
    assert not hand.is_valid_hand()


def test_check_hand_flush():
    hand = Pokerhand(['5D', 'KD', '6D', '4D', '10D'])
    assert hand.check_flush()


def test_check_hand_no_flush():
    hand = Pokerhand(['7S', '10D', '5H', '3C', 'KS'])
    assert not hand.check_flush()


def test_check_straight():
    hand = Pokerhand(['AC', '2C', '3C', '4S', '5S'])
    assert hand.check_straight()


def test_check_not_straight():
    hand = Pokerhand(['3C', '2C', '6C', '4S', '8S'])
    assert not hand.check_straight()


def test_check_not_straight_pairs():
    hand = Pokerhand(['3C', '3C', '6C', '6S', '8S'])
    assert not hand.check_straight()


def test_check_not_straight_same_ranks():
    hand = Pokerhand(['AC', 'AC', 'AC', 'AS', 'AS'])
    assert not hand.check_straight()


def test_check_royal():
    hand = Pokerhand(['AH', '10D', 'JC', 'QS', 'KS'])
    assert hand.check_royal()


def test_check_not_royal():
    hand = Pokerhand(['AH', '10D', '3C', '4S', 'JS'])
    assert not hand.check_royal()


def test_get_hand_royal_flush():
    hand = Pokerhand(['AS', '10S', 'JS', 'QS', 'KS'])
    assert hand.get_hand() == 10


def test_get_hand_straight_flush():
    hand = Pokerhand(['AS', '2S', '3S', '4S', '5S'])
    assert hand.get_hand() == 9


def test_get_hand_four_of_a_kind():
    hand = Pokerhand(['AS', 'AS', 'AS', 'AS', '5S'])
    assert hand.get_hand() == 8


def test_get_hand_full_house():
    hand = Pokerhand(['4S', '4S', '4S', 'AS', 'AS'])
    assert hand.get_hand() == 7


def test_get_hand_flush():
    hand = Pokerhand(['4H', '8H', '2H', '9H', '7H'])
    assert hand.get_hand() == 6


def test_get_hand_straight():
    hand = Pokerhand(['2H', '3C', '4S', '5H', '6D'])
    assert hand.get_hand() == 5


def test_get_hand_three_of_a_kind():
    hand = Pokerhand(['6S', '6H', '7C', 'JD', '6D'])
    assert hand.get_hand() == 4


def test_get_hand_check_two_pair():
    hand = Pokerhand(['3H', '8S', '8H', '9C', '3D'])
    assert hand.get_hand() == 3


def test_get_hand_one_pair():
    hand = Pokerhand(['AS', '10S', '5H', '10C', '6S'])
    assert hand.get_hand() == 2


def test_get_hand_high_card():
    hand = Pokerhand(['AS', '10S', '5H', '7C', '6S'])
    assert hand.get_hand() == 1
