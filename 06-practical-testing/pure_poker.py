# pylint: disable=line-too-long
# Type hinting: functie par & return values. Bij nieuwe variablen.

from typing import List, Dict, Set, Tuple


RANKS_DICT: Dict[str, str] = {'A':'ace', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', 'J':'jack', 'Q':'queen', 'K':'king'}
SUITS_DICT: Dict[str, str] = {'C':'clubs', 'H': 'hearts', 'S':'spades', 'D':'diamonds'}


def check_user_input(card: str) -> bool:
    check_input: bool = True
    rank, suit = card[:-1], card[-1]
    if rank not in RANKS_DICT or suit not in SUITS_DICT:
        check_input = False
    return check_input


def determine_hand_value(chosen_cards: List[str]):
    list_ranks, list_suits = split_rank_suit(chosen_cards)
    dict_possible_values: Dict[str, bool] = {
        'royal flush' : check_royal_flush(list_ranks, list_suits),
        'straigt flush' : check_straight_flush(list_ranks, list_suits),
        'four of a kind' : check_four_of_a_kind(list_ranks, list_suits),
        'full house' : check_full_house(list_ranks, list_suits),
        'flush' : check_flush(list_ranks, list_suits),
        'straight' : check_straight(list_ranks, list_suits),
        'three of a kind' : check_three_of_a_kind(list_ranks, list_suits),
        'two pair' : check_two_pair(list_ranks, list_suits),
        'one pair' : check_one_pair(list_ranks, list_suits),
        'high card' : True
    }


    for key in dict_possible_values:
        if dict_possible_values[key] == True:
            return key


def split_rank_suit(chosen_cards: List[str]) -> Tuple[List[str], List[str]]:
    list_ranks: List[str] = [] 
    list_suits: List[str] = []
    for card in chosen_cards:
        list_ranks.append(card[:-1])
        list_suits.append(card[-1])
    return list_ranks, list_suits


def check_royal_flush(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a royal flush.
    Characteristics: same suit and a straight flush that goes from 10 to ace. The highest ranking hand in the game.
    """
    royal_flush: bool = False
    royal_flush_ranks_sequence: List[str] = ['10','J','Q','K','A']

    if len(set(list_suits)) == 1:
        if len(set(list_ranks)) == 5:
            for item in list_ranks:
                if item in royal_flush_ranks_sequence:
                    royal_flush = True
                else:
                    royal_flush = False
                    break
    return royal_flush



def check_straight_flush(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a straight flush.
    Characteristics: It's a straight and a flush at the same time; five adjacent cards of the same suit.
    Returns an undefined value for a royal flush.
    """
    ranks_sequence: List[str] = []


    if len(set(list_suits)) > 1 or len(set(list_ranks)) < 5:
        return False


    if check_royal_flush(list_ranks, list_suits):
        return False


    for key in RANKS_DICT:
        ranks_sequence.append(key)


    index_ranks_list: List[int] = []
    for rank in list_ranks:
        index_ranks_list.append(ranks_sequence.index(rank))
    index_ranks_list.sort()

    lowest_rank: str = ranks_sequence[index_ranks_list[0]]
    highest_rank: str = ranks_sequence[index_ranks_list[-1]]


    for index in range(9):
        lowest_value: str = ranks_sequence[index]
        highest_value: str = ranks_sequence[index+4]
        if lowest_value == lowest_rank and highest_value == highest_rank:
            return True


    return False


def check_four_of_a_kind(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a four of a kind.
    Characteristics: four of any rank.
    """
    counting_dict: Dict[str, int] = {}
    counting_list: List[int] = []
    if len(set(list_ranks)) == 2:
        for item in list_ranks:
            counting_dict[item] = counting_dict.get(item, 0) + 1
        for value in counting_dict.values():
            counting_list.append(value)
        if all(value in counting_list for value in [4, 1]):
            return True
    return False


def check_full_house(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a full house.
    Characteristics: a three of a kind and one pair in the same hand.
    """
    counting_dict: Dict[str, int] = {}
    if len(set(list_ranks)) == 2:
        for item in list_ranks:
            counting_dict[item] = counting_dict.get(item, 0) + 1
        if set(counting_dict.values()) == {2, 3}:
            return True
    return False


def check_flush(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a flush.
    Characteristics: all the cards are of the same suit.
    """
    return len(set(list_suits)) == 1


def check_straight(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a straight.
    Characteristics: ranks are in a continuous sequence.
    """
    straight: bool = False
    ranks_sequence: List[str] = []


    if len(set(list_ranks)) != 5:
        return False


    for key in RANKS_DICT:
        ranks_sequence.append(key)

    index_ranks_list = []
    for rank in list_ranks:
        index_ranks_list.append(ranks_sequence.index(rank))
    index_ranks_list.sort()

    lowest_highest_rank: list[str] = [ranks_sequence[index_ranks_list[0]], ranks_sequence[index_ranks_list[-1]]]

    if lowest_highest_rank in [
        ['A', '5'],
        ['2', '6'],
        ['3', '7'],
        ['4', '8'],
        ['5', '9'],
        ['6', '10'],
        ['7', 'J'],
        ['8', 'Q'],
        ['9', 'K'],
    ]:
        straight: bool = True
    elif {'10','J','Q','K','A'} == set(list_ranks):
        straight: bool = True
    
    return straight


def check_three_of_a_kind(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a three of a kind.
    Characteristics: three of one rank.
    Note: a three of a kind with a one pair combination is a full house. In this case this will return False.
    """
    counting_dict: Dict[str, int] = {}
    if len(set(list_ranks)) == 3:
        for item in list_ranks:
            counting_dict[item] = counting_dict.get(item, 0) + 1    
    if 3 in counting_dict.values():
        return True
    return False


def check_two_pair(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a two pair.
    Characteristics: two pairs of ranked cards.
    """
    two_pair: bool = False
    counting_dict: Dict[str, int] = {}
    counting_list: List[int] = []
    if len(set(list_ranks)) == 3:
        for item in list_ranks:
            counting_dict[item] = counting_dict.get(item, 0) + 1
        for value in counting_dict.values():
            counting_list.append(value)
        if all(value in counting_list for value in [2, 1]):
            two_pair = True
    return two_pair


def check_one_pair(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a one pair.
    Characteristics: one pair of ranked cards.
    note: a combination with two times one pair is a two pair. In this case this will return False.
    A combination with an one pair and a three of a kind is a full house. In this case this will return False.
    """
    return len(set(list_ranks)) == 4


