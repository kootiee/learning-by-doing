# === Game of cards ===

# - Task:
#   - Write a function : 'parse_card'.
#   - This function can take short description of a playing card.
#   - This function returns a dictionary of data about that card.
#   - Write a full set of tests for this function.

# - Restrictions:
#   - Not allowed to exercise the function any other way. No print function, no writing to file, no main(), nothing.
#   - Not allowed: import guard. You are not allowed to python my_program.py (entry point (the command line).
#   - Allowed: imports, functions, constans and decorators.
#   - Run tests in the debugger, but this is not necessary.
#   - You can write as many other functions as you like, but parse_card should be the entry point to your module. If parse_card calls other things, that's cool, but not necessary.
#   - 'parse_card' should take one parameter, the string containing the short description of the card.
#   - Valid ranks (nummer) in the short description are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K.
#   - Valid suits (symbolen/kleur) in the short description are C, D, H, S.
#   - If the input string cannot be correctly parsed, or is invalid in some way, the 'parse_card' should raise a ValueError.
#   - The description must correctly use 'a' or 'an' depending on whether the written name of the rank starts with a vowel.
#   - Each test function can only contain one assert (tests with a condition).
#   - There is no set limit on how many tests you can write. Write as many or as few as you think are required to prove that your function works as you intend.
#   - No global variables.


RANK_DICT = {'A':'ace', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', 'J':'jack', 'Q':'queen', 'K':'king'}
SUITS_DICT = {'C':'clubs', 'H': 'hearts', 'S':'spades', 'D':'diamonds'}


def parse_card(card_description):
    rank, suit = card_description[0], card_description[1]
    description_value = f'a{"n" if rank in ("8","A") else ""} {RANK_DICT[rank]} of {SUITS_DICT[suit]}'
    return {
        'rank': rank,
        'suit': SUITS_DICT[suit],
        'description': description_value
    }

