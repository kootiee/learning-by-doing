#Red Green refactor
#TDD
#alle test functies begint met test_. Worden vanzelf aangeroepen door PyTest.
#je importeert eerst voordat je een test uitvoert
#assert is een conditie en een python keyword

from card import parse_card

def test_parse_card_5H():
    assert parse_card('5H') == {
        "rank": "5",
        "suit": "hearts",
        "description": "a five of hearts"
    }


def test_rank_2():
    assert parse_card('2H') == {
        'rank': '2',
        'suit': 'hearts',
        'description': 'a two of hearts'
    }


def test_rank_4():
    assert parse_card('4H') == {
        'rank': '4',
        'suit': 'hearts',
        'description': 'a four of hearts'
    }

