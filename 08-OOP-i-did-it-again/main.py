from pokerhand import Pokerhand
from pokergame import Pokergame


def main():
    print_display()
    Pokerhand_instances = get_players_input()
    print_game_result(Pokerhand_instances)


def print_display() -> None:
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                                                            ║
    ║                  WELCOME TO POKER GAME!                    ║
    ║                                                            ║
    ╠════════════════════════════════════════════════════════════╣
    ║                                                            ║
    ║  Get ready for some fun! Each player will enter 5 cards.   ║
    ║                                                            ║
    ║  Here are the available cards to choose from:              ║
    ║                                                            ║
    ║     ♠ Spades: A 2 3 4 5 6 7 8 9 10 J Q K                   ║
    ║     ♦ Diamonds: A 2 3 4 5 6 7 8 9 10 J Q K                 ║
    ║     ♣ Clubs: A 2 3 4 5 6 7 8 9 10 J Q K                    ║
    ║     ♥ Hearts: A 2 3 4 5 6 7 8 9 10 J Q K                   ║
    ║                                                            ║
    ╚════════════════════════════════════════════════════════════╝
    """)


def get_players_input() -> list[Pokerhand]:
    pokerhand_instances: list[Pokerhand] = []
    for _ in range(2):
        cards = input("Please enter your five cards (e.g., 2H KH AS 9C 5D): ")
        cards_list = cards.upper().split()

        hand_instance = Pokerhand(cards_list)
        if not hand_instance.is_valid_hand():
            print(
                f"Invalid hand: {' '.join(cards_list)}."
                "Thanks for playing! The game is now ending."
                )
            break

        pokerhand_instances.append(hand_instance)

    return pokerhand_instances


def print_game_result(pokerhand_instances: list[Pokerhand]):
    game = Pokergame(pokerhand_instances[0], pokerhand_instances[1])
    winner, loser = game.compare_hands()

    if loser == ['Tie']:
        print("""
        ╔════════════════════════════════════════════════════════════╗
        ║                                                            ║
        ║                    IT'S A TIE GAME!                        ║
        ║                                                            ║
        ║   Both players have the same hand, so no one wins!         ║
        ║                                                            ║
        ║        Player 1 Hand: {player1_hand}                       ║
        ║        Player 2 Hand: {player2_hand}                       ║
        ║                                                            ║
        ║        Try again for a winner next time!                   ║
        ║                                                            ║
        ╚════════════════════════════════════════════════════════════╝
        """.format(
            player1_hand=' '.join(winner[0]),
            player2_hand=' '.join(winner[1])
        ))
    else:
        print("""
        ╔════════════════════════════════════════════════════════════╗
        ║                                                            ║
        ║                    THE WINNER IS {winner[0]}!              ║
        ║                                                            ║
        ║        {winner[0]} won with a {winner[1]} hand.            ║
        ║        Congratulations, {winner[0]}!                       ║
        ║                                                            ║
        ║        Player 1 Hand: {player1_hand}                       ║
        ║        Player 2 Hand: {player2_hand}                       ║
        ║                                                            ║
        ║                    THE LOSER IS {loser[0]}!                ║
        ║        {loser[0]} lost with a {loser[1]} hand.             ║
        ║                                                            ║
        ╚════════════════════════════════════════════════════════════╝
        """.format(
            winner=winner[0],
            loser=loser[0],
            player1_hand=' '.join(winner[1]),
            player2_hand=' '.join(loser[1])
        ))


if __name__ == '__main__':
    main()

# ============================================================================
