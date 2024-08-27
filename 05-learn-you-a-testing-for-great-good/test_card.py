from card import parse_card

#Welke nummers/items veranderen het gedrag.
#Kijken naar de omslagpunten, niet alles hoeft exact getest te worden.
#OP basis van ervaring en logica
#verdiepen in f-strings!
#constante variables zet je onder je import neer. Ligt op hetzelfde indentatie als de functie. Als een soort 'global' variable. Je hoeft ze dan ook niet aan te roepen bij de parameters. Het staat op module/bestand-niveau.
#Elke python-bestandje is een module. En elke mapje/directory (__init__.py) is een package
#constante variable -> schrijf je in all-caps (conventie)
#bij elke WERKENDE test -> git commit

def test_rank_2H():
    assert parse_card('2H') == {
        'rank': '2',
        'suit': 'hearts',
        'description': 'a two of hearts'
    }


def test_rank_4H():
    assert parse_card('4H') == {
        'rank': '4',
        'suit': 'hearts',
        'description': 'a four of hearts'
    }


def test_rank_AH():
    assert parse_card('AH') == {
        'rank': 'A',
        'suit': 'hearts',
        'description': 'an ace of hearts'
    }


def test_rank_QH():
    assert parse_card('QH') == {
        'rank': 'Q',
        'suit': 'hearts',
        'description': 'a queen of hearts'
    }


def test_rank_2C():
    assert parse_card('2C') == {
        'rank': '2',
        'suit': 'clubs',
        'description': 'a two of clubs'
    }


def test_rank_4C():
    assert parse_card('4C') == {
        'rank': '4',
        'suit': 'clubs',
        'description': 'a four of clubs'
    }


def test_rank_AC():
    assert parse_card('AC') == {
        'rank': 'A',
        'suit': 'clubs',
        'description': 'an ace of clubs'
    }


def test_rank_QC():
    assert parse_card('QC') == {
        'rank': 'Q',
        'suit': 'clubs',
        'description': 'a queen of clubs'
    }


def test_rank_2D():
    assert parse_card('2D') == {
        'rank': '2',
        'suit': 'diamonds',
        'description': 'a two of diamonds'
    }


def test_rank_4D():
    assert parse_card('4D') == {
        'rank': '4',
        'suit': 'diamonds',
        'description': 'a four of diamonds'
    }


def test_rank_AD():
    assert parse_card('AD') == {
        'rank': 'A',
        'suit': 'diamonds',
        'description': 'an ace of diamonds'
    }


def test_rank_QD():
    assert parse_card('QD') == {
        'rank': 'Q',
        'suit': 'diamonds',
        'description': 'a queen of diamonds'
    }

def test_rank_2S():
    assert parse_card('2S') == {
        'rank': '2',
        'suit': 'spades',
        'description': 'a two of spades'
    }


def test_rank_4S():
    assert parse_card('4S') == {
        'rank': '4',
        'suit': 'spades',
        'description': 'a four of spades'
    }


def test_rank_AS():
    assert parse_card('AS') == {
        'rank': 'A',
        'suit': 'spades',
        'description': 'an ace of spades'
    }


def test_rank_QS():
    assert parse_card('QS') == {
        'rank': 'Q',
        'suit': 'spades',
        'description': 'a queen of spades'
    }

