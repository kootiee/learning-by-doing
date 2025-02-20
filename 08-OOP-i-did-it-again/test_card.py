from card import Card
import pytest


def test_get_rank_number():
    card = Card('2H')
    assert card.rank == '2'


def test_get_rank_letter():
    card = Card('AD')
    assert card.rank == 'A'


def test_get_rank_invalid():
    card = Card('11S')
    assert card.rank == '11'


def test_get_rank_invalid_symbol():
    card = Card('!S')
    assert card.rank == '!'


def test_get_rank_invalid_excessive_input():
    with pytest.raises(ValueError):
        Card('kokoD')


def test_get_rank_invalid_less_input():
    card = Card('1H')
    assert card.rank == '1'


def test_get_rank_invalid_no_input():
    with pytest.raises(ValueError):
        Card('')


def test_get_suit():
    card = Card('5C')
    assert card.suit == 'C'


def test_get_suit_invalid():
    card = Card('4K')
    assert card.suit == 'K'


def test_get_suit_invalid_symbol():
    card = Card('A@')
    assert card.suit == '@'


def test_get_suit_invalid_excessive_input():
    with pytest.raises(ValueError):
        Card('2Koko')


def test_get_suit_invalid_no_input():
    with pytest.raises(ValueError):
        Card('2')


def test_is_valid_card():
    card = Card('5H')
    assert card.is_valid_card()


def test_is_invalid_card():
    card = Card('KA')
    assert not card.is_valid_card()


def test_card_greater_than():
    card1 = Card('10H')
    card2 = Card('5H')
    assert card1 > card2


def test_card_less_than():
    card1 = Card('7H')
    card2 = Card('4S')
    assert card2 < card1
