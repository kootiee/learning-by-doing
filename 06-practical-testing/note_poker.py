def determine_card_value(chosen_cards): 
    list_rank, list_suit = sort_rank_suit(chosen_cards)
    dict_possible_values = {
        'high card' : True,
        'one pair' : check_one_pair(list_rank),
        'two pair' : check_two_pair(list_rank),
        'three of a kind' : check_three_of_a_kind(list_rank),
        'straight' : check_straight(list_rank),
        'flush' : check_flush(list_suit),
        'full house' : check_full_house(list_rank),
        'four of a kind' : check_four_of_a_kind(list_rank),
        'straigt flush' : check_straight_Flush(list_suit, list_rank),
        'royal flush' : check_royal_flush(list_suit, list_rank)
    }

    for key in dict_possible_values:
        if dict_possible_values[key] == True:
            return key #Er kunnen meerdere True zijn. Bekijk de hoogst scorende hand.
    

def sort_rank_suit(chosen_cards):
    list_rank, list_suit = [], []
    for card in chosen_cards:
        list_rank.append(card[:-1])
        list_suit.append(card[-1])
    return list_rank, list_suit


def check_one_pair(list_rank):
    One_Pair = False
    if len(set(list_rank)) == 4:
        One_Pair = True
    return One_Pair


def check_two_pair(list_rank):
    Two_Pair = True
    counting_dict = {}
    if len(set(list_rank)) == 3:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
            if counting_dict[item] > 2:
                Two_Pair = False
    return Two_Pair


def check_three_of_a_kind(list_rank):
    Three_of_a_kind = False
    counting_dict = {}
    if len(set(list_rank)) == 3:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
            if counting_dict[item] > 3:
                Three_of_a_kind = True
    return Three_of_a_kind


def check_straight(list_rank):
    Straight = False
    rank_sequence = ''
    for key in RANK_DICT:
        rank_sequence + key
    rank_sequence + 'A'

    index_rank_list= []
    for item in list_rank:
        index_rank_list.append(rank_sequence.index(item))
    sorted_index_rank_list = index_rank_list.sort()

    user_input_rank_sequence = ''
    for index in sorted_index_rank_list:
         user_input_rank_sequence + rank_sequence[index]
    if user_input_rank_sequence in rank_sequence:
        Straight = True
    return Straight


def check_flush(list_suit):
    Flush = False
    if len(set(list_suit)) == 1:
        Flush = True
    return Flush


def check_full_house(list_rank):
    Full_House = False
    counting_dict, counting_list = {}, []
    if len(set(list_rank)) == 2:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
        for value in counting_dict.values():
            counting_list.append(value)
        if all(value in counting_list for value in [2, 3]):
            Full_House = True
    return Full_House


def check_four_of_a_kind(list_rank):
    Four_of_a_kind = False
    counting_dict, counting_list = {}, []
    if len(set(list_rank)) == 2:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
        for value in counting_dict.values():
            counting_list.append(value)
        if all(value in counting_list for value in [4, 1]):
            Full_House = True
    return Four_of_a_kind


def check_straight_Flush(list_suit, list_rank):
    Straight_Flush = False
    rank_sequence = ''

    if len(set(list_suit)) == 1:
        for key in RANK_DICT:
            rank_sequence + key
        rank_sequence + 'A'

        index_rank_list= []
        for item in list_rank:
            index_rank_list.append(rank_sequence.index(item))
        sorted_index_rank_list = index_rank_list.sort()

        user_input_rank_sequence = ''
        for index in sorted_index_rank_list:
            user_input_rank_sequence + rank_sequence[index]
        if user_input_rank_sequence in rank_sequence:
            Straight_Flush = True

    return Straight_Flush


def check_royal_flush(list_suit, list_rank):
    Royal_Flush = False
    rank_sequence = ''
    Royal_Flush_rank_sequence = '10JQKA'

    if len(set(list_suit)) == 1:
        for key in RANK_DICT:
            rank_sequence + key
        rank_sequence + 'A'

        index_rank_list= []
        for item in list_rank:
            index_rank_list.append(rank_sequence.index(item))
        sorted_index_rank_list = index_rank_list.sort()

        user_input_rank_sequence = ''
        for index in sorted_index_rank_list:
            user_input_rank_sequence + rank_sequence[index]
        if user_input_rank_sequence in Royal_Flush_rank_sequence:
            Royal_Flush = True

    return Royal_Flush




# ----------------------------------------




def check_one_pair(list_rank):
    One_Pair = False
    if len(set(list_rank)) == 4:
        One_Pair = True
    return One_Pair


def check_two_pair(list_rank):
    Two_Pair = True
    counting_dict = {}
    if len(set(list_rank)) == 3:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
            if counting_dict[item] > 2:
                Two_Pair = False
    return Two_Pair


def check_three_of_a_kind(list_rank):
    Three_of_a_kind = False
    counting_dict = {}
    if len(set(list_rank)) == 3:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
            if counting_dict[item] > 3:
                Three_of_a_kind = True
    return Three_of_a_kind


def check_straight(list_rank):
    Straight = False
    rank_sequence = ''
    for key in RANK_DICT:
        rank_sequence + key
    rank_sequence + 'A'

    index_rank_list= []
    for item in list_rank:
        index_rank_list.append(rank_sequence.index(item))
    sorted_index_rank_list = index_rank_list.sort()

    user_input_rank_sequence = ''
    for index in sorted_index_rank_list:
         user_input_rank_sequence + rank_sequence[index]
    if user_input_rank_sequence in rank_sequence:
        Straight = True
    return Straight


def check_flush(list_suit):
    Flush = False
    if len(set(list_suit)) == 1:
        Flush = True
    return Flush


def check_full_house(list_rank):
    Full_House = False
    counting_dict, counting_list = {}, []
    if len(set(list_rank)) == 2:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
        for value in counting_dict.values():
            counting_list.append(value)
        if all(value in counting_list for value in [2, 3]):
            Full_House = True
    return Full_House


def check_four_of_a_kind(list_rank):
    Four_of_a_kind = False
    counting_dict, counting_list = {}, []
    if len(set(list_rank)) == 2:
        for item in list_rank:
            counting_dict[item] = counting_dict.get(item, 0) + 1
        for value in counting_dict.values():
            counting_list.append(value)
        if all(value in counting_list for value in [4, 1]):
            Full_House = True
    return Four_of_a_kind







