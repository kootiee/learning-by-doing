# De verschillende onderdelen van het project -> de code:
#   -> Het programma moet worden opgesplitst in drie modules, waaronder main.
#   -> De andere modules die elk een class bevatten, kunnen niet printen,
#      invoeren en openen.
#   -> Main moet zo simpel mogelijk zijn.

#   MAIN:
#   - Het scherm die de spelers zien.

#   MAIN:
#   - Het scherm waarin de eerste speler zijn kaarten invoerd.
#   - Het scherm waarin de tweede speler zijn kaarten invoerd.
#   - Invoer van elke speler is een list:
#       - De list bestaat uit 5 elementen met datatype string.
#       - Elk element representeert een kaart, wat bestaat uit rank en suit.
#       - De list representeert een hand van kaarten.

#   - Er moet eerst gekeken of de invoer juist is, anders moet er een reactie
#     worden gegeven. Die kan bestaan uit:
#       - Een nieuwe invoer.
#       - Stop het programma.

#   - Invoer moet verwekt worden:
#       - Er moet per speler gekeken worden.
#       - Er moet specifiek worden gekeken naar de ranks en suits.
#           - Ranks:
#               - Straight that goes from ten to ace.
#               - Straight where all five cards form a continuous sequence.
#               - The amount of pairs -> one pair and two pair.
#               - The amount of the same ranks -> three of a kind and
#                  four of a kind.
#               - Full house -> three of a kind + one pair
#           - Suits:
#               - Straight flush -> straight + flush.
#               - Royal flush -> straight that goes from ten to ace + flush
#           - Combination:
#               - Full house -> three of a kind + one pair
#           - No pattern:
#               - High card

#   - De winnaar en verliezer met desbetreffende hand moet berekend worden.
#   - Anders moet er gekeken worden of er gelijk spel is.

#   MAIN:
#   - Het scherm die het resultaat uitprint.


# CLASS: POKERGAME
# - atrribute: hand (verbonden aan een speler. Speler is niet relevant.
#   Meer info is niet nodig (abstractie).)
# - method: het vergelijken van beide handen -> compare_hands()
# - method: het geven van een printbare winnaar en verliezer ->
#           - bekijk hiervoor __str__() (niet verplicht)

# CLASS: POKERHAND
# - attribute: de lijst met kaarten.
# - method: checken of de invoer van VIJF kaarten juist is -> is_valid_hand()
# - method: berekenen van de hand -> get_hand() -> functie kan in de __init__()
#           - resultaat opslaan in een attribute
# - method: __gt__()
# - method: __lt__()

# CLASS: CARD
# - attribute: card_string
# - attribute: card_suit
# - attribute: card_rank
# - method: checken of de invoer van de kaart juist is -> is_valid_card()
# - method: get_suit() -> functie kan in de __init__()
# - method: get_rank() -> functie kan in de __init__()
# - method: __gt__()
# - method: __lt__()

# TYPE HINT!!!! <---- PARA'S & RETURNS, ATTRIBUTES

# classes (enkelvoud) zijn geen acties. Het is een ding/object.
# -> verzameling van informatie en acties die een doel bereiken.
# TYPE HINT!!!! <---- PARA'S & RETURNS, ATTRIBUTES
