from card import Card
from collections import Counter


ROYAL: list[int] = [1, 10, 11, 12, 13]


class Pokerhand:
    def __init__(self, cards: list[str]):
        self.cards = [Card(card_str) for card_str in cards]  # 1
        self.ranks = sorted(
            [card.get_rank_value() for card in self.cards])  # 2
        self.hand = self.get_hand()

    def is_valid_hand(self):
        return len(self.cards) == 5 and \
            all(card.is_valid_card() for card in self.cards)  # 3

    def check_flush(self):
        return len(set(card.get_suit() for card in self.cards)) == 1

    def check_straight(self):
        for index, rank in enumerate(self.ranks[1:], 1):  # 4
            if rank - self.ranks[index - 1] != 1:
                return False
        return True

    def check_royal(self):
        if self.ranks == ROYAL:
            return True
        return False

    def get_hand(self):
        if self.check_royal() and self.check_flush():
            return 10
        elif self.check_straight() and self.check_flush():
            return 9
        elif self._check_pairs() == 8 or self._check_pairs() == 7:
            return self._check_pairs()
        elif self.check_flush():
            return 6
        elif self.check_straight():
            return 5
        else:
            return self._check_pairs()

    def _check_pairs(self):
        counted_ranks_dict = Counter(self.ranks)
        rank_counts = list(counted_ranks_dict.values())
        if 4 in rank_counts:
            return 8
        elif 3 in rank_counts and 2 in rank_counts:
            return 7
        elif 3 in rank_counts:
            return 4
        elif rank_counts.count(2) == 2:
            return 3
        elif 2 in rank_counts:
            return 2
        return 1

    def __gt__(self, other: 'Pokerhand'):
        if self.get_hand() > other.get_hand():
            return True
        return False

    def __lt__(self, other: 'Pokerhand'):
        if self.get_hand() < other.get_hand():
            return True
        return False


# ============================================================================
# 1 - For each card_str in the cards list, the code is creating a new instance
# 2 - The sorted() function calls the __lt__ method to compare each pair
#     of cards and sort them in ascending order based on their rank.
#     of the Card class by calling Card(card_str).
# 3 - The all() function takes an iterable and returns True if all elements
#      are True.
# 4 - enumerate(iterable, start)

# ============================================================================
# - Ranks:
#   - Straight that goes from ten to ace.
#   - Straight where all five cards form a continuous sequence.
#   - The amount of pairs -> one pair and two pair.
#   - The amount of the same ranks -> three of a kind and four of a kind.
#   - Full house -> three of a kind + one pair

# - Suits:
#   - Straight flush -> straight + flush.
#   - Royal flush -> straight that goes from ten to ace + flush

# - Combination:
#   - Full house -> three of a kind + one pair

#   - No pattern:
#     - High card
