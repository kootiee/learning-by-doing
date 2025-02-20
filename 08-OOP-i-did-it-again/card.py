from typing import Dict

RANKS: Dict[int, str] = {
    1: 'A', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: '10', 11: 'J',
    12: 'Q', 13: 'K'
    }
SUITS: Dict[int, str] = {
    1: 'H', 2: 'D', 3: 'C', 4: 'S'
    }


class Card:

    def __init__(self, card: str) -> None:
        self.card: str = card
        self.rank: str = self._get_rank()
        self.suit: str = self.get_suit()

    def _get_rank(self) -> str:
        if len(self.card) <= 1 or len(self.card) > 3:
            raise ValueError
        return self.card[:-1]  # 1

    def get_rank_value(self) -> int:
        for key, value in RANKS.items():
            if value == self.rank:
                return key
        raise ValueError

    def get_suit(self) -> str:
        if len(self.card) <= 1 or len(self.card) > 3:
            raise ValueError
        return self.card[-1]  # 2

    def is_valid_card(self) -> bool:
        return self.rank in RANKS.values() and self.suit in SUITS.values()  # 3

    def __gt__(self, other: 'Card') -> bool:
        if self.get_rank_value() > other.get_rank_value():
            return True
        return False

    def __lt__(self, other: 'Card') -> bool:
        if self.get_rank_value() < other.get_rank_value():
            return True
        return False


# ============================================================================
# 1 - All but last character.
# 2 - Last character.
# 3 - values() gives a list of valid RANKS or SUITS and checks if it exists
#      in that list.
