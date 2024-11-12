from pure_rummy import check_user_input, check_three_of_a_kind, check_four_of_a_kind, check_straight_three, check_straight_four

def test_check_user_input_valid_rank_and_suit():
    assert check_user_input('AC') == True


def test_check_user_input_invalid_rank_and_suit():
    assert check_user_input('11K') == False


def test_check_user_input_invalid_rank():
    assert check_user_input('BC') == False


def test_check_user_input_invalid_suit():
    assert check_user_input('9A') == False


def test_check_three_of_a_kind():
    assert check_three_of_a_kind(['A', 'A', '5', '8', '6', '7', 'A'], ['C', 'S', 'C', 'C', 'C','C','H']) == True


def test_check_three_of_a_kind_with_four_of_the_same_ranks():
    assert check_three_of_a_kind(['J', 'A', 'J', '8', 'J', '7', 'J'], ['C', 'S', 'C', 'C', 'C','C','H']) == False


def test_check_three_of_a_kind_with_two_of_the_same_ranks():
    assert check_three_of_a_kind(['Q', '10', 'K', 'Q', '9', '7', 'K'], ['C', 'S', 'C', 'C', 'C','C','H']) == False


def test_check_three_of_a_kind_with_same_ranks():
    assert check_three_of_a_kind(['K', 'K', 'K', 'K', 'K', 'K', 'K'], ['C', 'S', 'C', 'C', 'C','C','H']) == True


def test_check_four_of_a_kind():
    assert check_four_of_a_kind(['10', '9', '8', '7', '7', '7', '7'], ['C', 'S', 'C', 'C', 'C','C','H']) == True


def test_check_four_of_a_kind_with_five_of_the_same_ranks():
    assert check_four_of_a_kind(['9', '9', '8', '7', '9', '9', '9'], ['C', 'S', 'C', 'C', 'C','C','H']) == False


def test_check_four_of_a_kind_with_three_of_the_same_ranks():
    assert check_four_of_a_kind(['10', '9', '8', 'A', 'A', 'A', '7'], ['C', 'S', 'C', 'C', 'C','C','H']) == False


def test_check_four_of_a_kind_with_same_ranks():
    assert check_four_of_a_kind(['5', '5', '5', '5', '5', '5', '5'], ['C', 'S', 'C', 'C', 'C','C','H']) == True


def test_check_straight_three():
    assert check_straight_three(['AH', '2H', '3H', '4H', '5H', '6H', '7H']) == True


def test_check_not_straight_three():
    assert check_straight_three(['AH', '3H', '5H', '7H', '9H', 'JH', 'KH']) == False


def test_check_straight_three_with_two_adjacent_cards_of_the_same_suit():
    assert check_straight_three(['JC', 'AS', 'JC', '8C', 'JC', '7C', 'JH']) == False


def test_check_straight_three_with_four_adjacent_cards_of_the_same_suit():
    assert check_straight_three(['QC', '10S', 'KC', 'QC', '9C', '7C', 'KH']) == False


def test_check_straight_three_with_same_ranks():
    assert check_straight_three(['KC', 'KS', 'KC', 'KC', 'KC', 'KC', 'KH']) == False


def test_check_straight_four():
    assert check_straight_four(['AH', '3H', '5H', '7H', '9H', 'JH', 'KH']) == False


def test_check_not_straight_four():
    assert check_straight_four(['2H', '4H', '6H', '8H', '10H', 'JH', 'KH']) == False


def test_check_straight_fourh_with_three_adjacent_cards_of_the_same_suit():
    assert check_straight_four(['AH', '2H', '3H', '6H', '8H', '10H', '7H']) == False


def test_check_straight_fourh_with_five_adjacent_cards_of_the_same_suit():
    assert check_straight_four(['5H', '6H', '7H', '8H', '9H', '10H', 'AH']) == True