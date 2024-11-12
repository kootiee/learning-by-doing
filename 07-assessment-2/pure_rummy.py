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
    sorted_cards = sort_cards_based_on_rank(list_ranks, list_suits)
    dict_possible_values: Dict[str, bool] = {
        'three of a kind' : check_three_of_a_kind(list_ranks, list_suits),
        'four of a kind' : check_four_of_a_kind(list_ranks, list_suits),
        'straight three' : check_straight_three(sorted_cards),
        'straight four' : check_straight_four(sorted_cards),
    }

    hand_of_three = dict_possible_values['three of a kind'] or dict_possible_values['straight three']
    hand_of_four = dict_possible_values['four of a kind'] or dict_possible_values['straight four']
    if hand_of_three and hand_of_four:
        return 'won'
    else:
        return 'lose'



def split_rank_suit(chosen_cards: List[str]) -> Tuple[List[str], List[str]]:
    list_ranks: List[str] = [] 
    list_suits: List[str] = []
    for card in chosen_cards:
        list_ranks.append(card[:-1])
        list_suits.append(card[-1])
    return list_ranks, list_suits



def sort_cards_based_on_rank(list_ranks: List[str], list_suits: List[str]) -> list:
    ranks_sequence = []
    for key in RANKS_DICT:
        ranks_sequence.append(key)

    entered_seven_cards = []
    for (rank, suit) in zip(list_ranks, list_suits):
        entered_seven_cards.append([rank, suit, ranks_sequence.index(rank)])

    rank_index = 2
    for i in range(0, len(entered_seven_cards)): #length of the loop is equal to the number of cards.
        for j in range(i+1, len(entered_seven_cards)): #length of the loop is equal to the number of cards + 1.
            if entered_seven_cards[i][rank_index] >= entered_seven_cards[j][rank_index]: #entered_seven_cards is a list of lists. The first index represents the card, and the second index is the rank.
                entered_seven_cards[i][rank_index], entered_seven_cards[j][rank_index] = entered_seven_cards[j][rank_index], entered_seven_cards[i][rank_index] #sort the cards by rank.
    
    return entered_seven_cards



def check_three_of_a_kind(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a three of a kind.
    Characteristics: three of one rank.
    """
    counting_dict: Dict[str, int] = {}
    for item in list_ranks:
        counting_dict[item] = counting_dict.get(item, 0) + 1
    if 3 in counting_dict.values():
        return True
    elif 7 in counting_dict.values():
        return True
    return False



def check_four_of_a_kind(list_ranks: List[str], list_suits: List[str]) -> bool:
    """
    Checks if a hand is a four of a kind.
    Characteristics: four of any rank.
    """
    counting_dict: Dict[str, int] = {}
    counting_list: List[int] = []
    for item in list_ranks:
        counting_dict[item] = counting_dict.get(item, 0) + 1
    for value in counting_dict.values():
        counting_list.append(value)
    if 4 in counting_list:
        return True
    elif 7 in counting_list:
        return True
    return False



def check_straight_three(sorted_cards: List[str]) -> bool:
    """
    Checks if a hand is a straight three.
    Characteristics: a straight of three adjancent (rank) cards of the same suit. 
    """
    suit = 1
    for index in range(5): #Range is 5 because three adjacents cards are compared each time -> 0,1,2 / 1,2,3 / 2,3,4 / 3,4,5 / 4,5,6
        for card in sorted_cards:
            straight_lowest_highest_pair = (sorted_cards[index][0], sorted_cards[index + 2][0]) #Every set of three cards, the lowest and highest ranks are evaluated.
            if straight_lowest_highest_pair in [
                ('A', '3'),
                ('2', '4'),
                ('3', '5'),
                ('4', '6'),
                ('5', '7'),
                ('6', '8'),
                ('7', '9'),
                ('8', '10'),
                ('9', 'J'),
                ('10', 'Q'),
                ('J','K')
            ]:
                if sorted_cards[index][suit] == sorted_cards[index + 1 ][suit] == sorted_cards[index + 2][suit]: #Checks for the same suit.
                    return True
    return False



def check_straight_four(sorted_cards: List[str]) -> bool:
    """
    Checks if a hand is a straight four.
    Characteristics: a straight of four adjancent (rank) cards of the same suit. 
    """


    suit = 1
    for index in range(4): #Range is 4 because four adjacents cards are compared each time -> 0,1,2,3 / 1,2,3,4 / 2,3,4,5 / 3,4,5,6
        for card in sorted_cards:
            straight_lowest_highest_pair = (sorted_cards[index][0], sorted_cards[index + 3][0]) #Every set of four cards, the lowest and highest ranks are evaluated.
            if straight_lowest_highest_pair in [
                ('A', '4'),
                ('2', '5'),
                ('3', '6'),
                ('4', '7'),
                ('5', '8'),
                ('6', '9'),
                ('7', '10'),
                ('8', 'J'),
                ('9', 'Q'),
                ('10', 'K')
            ]:
                if sorted_cards[index][suit] == sorted_cards[index + 1 ][suit] == sorted_cards[index + 2][suit] == sorted_cards[index + 3][suit]:
                    return True
    return False