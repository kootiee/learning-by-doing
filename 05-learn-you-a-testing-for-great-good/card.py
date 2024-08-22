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


# import random

# def characteristics_of_the_card():
#     ranks = {1: ['A','ace'], 2: ['2','two'], 3: ['3','three'], 4: ['4','four'], 5: ['5','five'] , 6: ['6','six'] , 7: ['7', 'seven'], 8: ['8','eight'], 9: ['9','nine'], 10: ['10', 'ten'], 11: ['J', 'jack'], 12: ['Q', 'queen'], 13: ['K','king']}
#     suits = {1:['C','clubs'], 2:['H','hearts'], 3:['S','spades'], 4:['D','diamonds']}
#     return ranks, suits


# def random_ranks_and_suits(ranks, suits):
#     selected_ranks = ranks[random.randint(1, 13)]
#     selected_suits = suits[random.randint(1, 4)]
#     return selected_ranks, selected_suits


# def description_of_the_card(selected_ranks, selected_suits):
#     card_description = [selected_ranks[0], selected_suits[0], 'a'+selected_ranks[1]+'of'+selected_suits[1]]
#     return card_description
    

def parse_card(card_description):
    if card_description == '5H':
        return {"rank": '5', "suit": 'hearts', "description": 'a five of hearts'}
    elif card_description == '4H':
        return {'rank': '4', 'suit': 'hearts', 'description': 'a four of hearts'}
    elif card_description == '2H':
        return {'rank': '2', 'suit': 'hearts', 'description': 'a two of hearts'}

