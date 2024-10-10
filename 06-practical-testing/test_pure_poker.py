#Dekking van verschillende situaties (if/elif-statements)

from pure_poker import check_user_input, check_royal_flush, check_straight_flush, check_four_of_a_kind, check_full_house, check_flush, check_straight, check_three_of_a_kind, check_two_pair, check_one_pair

def test_check_user_input_rank_with_3_characters_rank_10():
    assert check_user_input('10C') == True


def test_check_user_input_rank_with_3_characters_rank_not_10():
    assert check_user_input('11C') == False


def test_check_user_input_rank_with_3_characters_rank_10_and_not_valid_suit():
    assert check_user_input('10Q') == False


def test_check_user_input_valid_rank_and_suit():
    assert check_user_input('AC') == True


def test_check_user_input_invalid_rank():
    assert check_user_input('1C') == False


def test_check_user_input_invalid_suit():
    assert check_user_input('AK') == False


def test_check_user_input_invalid_rank_and_suit():
    assert check_user_input('1Z') == False


def test_check_user_input_invald_card_length_one_characters():
    assert check_user_input('4') == False


def test_check_user_input_invald_card_length_four_characters():
    assert check_user_input('2CA5') == False


def test_check_royal_flush():
    assert check_royal_flush(['10', 'J', 'Q', 'K', 'A'], ['S', 'S', 'S', 'S', 'S']) == True


def test_check_not_royal_flush_double_ranks():
    assert check_royal_flush(['A', 'J', 'Q', 'K', 'A'], ['S', 'S', 'S', 'S', 'S']) == False


def test_check_not_royal_flush_different_suits():
    assert check_royal_flush(['A', 'J', 'Q', 'K', 'A'], ['H', 'D', 'S', 'S', 'C']) == False


def test_check_straight_flush():
    assert check_straight_flush(['A', '2', '3', '4', '5'], ['S', 'S', 'S', 'S', 'S']) == True


def test_check_straight_flush():
    assert check_straight_flush(['J', 'Q', 'K', '10', '9'], ['S', 'S', 'S', 'S', 'S']) == True


def test_check_four_of_a_kind():
    assert check_four_of_a_kind(['J', 'J', 'J', 'J', '5'], ['C', 'D', 'S', 'C', 'H']) == True


def test_check_four_of_a_kind_same_suit():
    assert check_four_of_a_kind(['J', 'J', 'J', 'J', '5'], ['C', 'C', 'C', 'C', 'C']) == True


def test_check_four_of_a_kind_same_rank():
    assert check_four_of_a_kind(['K', 'K', 'K', 'K', 'K'], ['C', 'D', 'S', 'C', 'H']) == False


def test_check_four_of_a_kind_three_of_the_same_ranks():
    assert check_four_of_a_kind(['J', 'J', 'J', '5', '5'], ['C', 'D', 'S', 'C', 'H']) == False


def test_check_full_house():
    assert check_full_house(['4', '4', '4', '8', '8'], ['H', 'D', 'C', 'S', 'D']) == True


def test_check_full_house_same_suit():
    assert check_full_house(['4', '4', '4', '8', '8'], ['H', 'H', 'H', 'H', 'H']) == True


def test_check_full_house_same_rank():
    assert check_full_house(['A', 'A', 'A', 'A', 'A'], ['H', 'D', 'C', 'S', 'D']) == False


def test_check_full_house_four_of_the_same_rank():
    assert check_full_house(['3', '3', '3', '3', 'A'], ['H', 'D', 'C', 'S', 'D']) == False


def test_check_flush():
    assert check_flush(['4', '8', '2', '8', '8'], ['H', 'H', 'H', 'H', 'H']) == True


def test_check_flush_different_kind_of_suits():
    assert check_flush(['4', '8', '2', '8', '8'], ['H', 'S', 'C', 'D', 'H']) == False


def test_check_flush_pairs_of_ranks():
    assert check_flush(['A', '2', '5', 'K', 'J'], ['H', 'H', 'C', 'C', 'D']) == False


def test_check_straight():
    assert check_straight(['2', '3', '4', '5', '6'], ['H', 'C', 'S', 'S', 'D']) == True

def test_check_straight_lowest():
    assert check_straight(['A', '2', '3', '4', '5'], ['H', 'D', 'S', 'S', 'C']) == True


def test_check_straight_highest():
    assert check_straight(['10', 'J', 'Q', 'K', 'A'], ['D', 'S', 'S', 'C', 'C']) == True


def test_check_not_straight_with_A_highest():
    assert check_straight(['2', '4', '7', 'K', 'A'], ['D', 'S', 'S', 'C', 'C']) == False


def test_check_not_straight_one_pair_rank():
    assert check_straight(['J', 'Q', 'K', 'K', 'A'], ['D', 'S', 'S', 'C', 'C']) == False


def test_check_not_straight_not_sequence():
    assert check_straight(['3', '6', '9', 'Q', 'A'], ['D', 'S', 'S', 'C', 'C']) == False


def test_check_three_of_a_kind():
    assert check_three_of_a_kind(['6','6','7','J','6'], ['S','H','C','D','D']) == True


def test_check_not_three_of_a_kind():
    assert check_three_of_a_kind(['5','4','7','K','6'], ['S','H','C','D','D']) == False


def test_check_three_of_a_kind_and_two_of_a_kind():
    assert check_three_of_a_kind(['8','8','8','Q','Q'], ['S','H','C','D','D']) == False


def test_check_two_pair():
    assert check_two_pair(['3','8','8','9','3'], ['H','C','H','S','D']) == True


def test_check_not_two_pair_but_one_pair():
    assert check_two_pair(['A','8','8','9','10'], ['H','C','H','S','D']) == False


def test_check_not_two_pair_but_three_of_a_kind():
    assert check_two_pair(['A','A','A','8','2'], ['H','C','H','S','D']) == False


def test_check_one_pair():
    assert check_one_pair(['A','10','5','10','6'], ['H','C','H','S','D']) == True


def test_check_not_one_pair():
    assert check_one_pair(['A','9','5','10','6'], ['H','C','H','S','D']) == False


def test_check_one_pair_and_one_pair():
    assert check_one_pair(['9','9','5','10','10'], ['H','C','H','S','D']) == False


def test_check_one_pair_and_three_of_a_kind():
    assert check_one_pair(['5','5','5','A','A'], ['H','C','H','S','D']) == False
