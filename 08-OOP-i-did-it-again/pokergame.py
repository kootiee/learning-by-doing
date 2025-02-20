from pokerhand import Pokerhand

HAND_VALUES: dict[int, str] = {
   1: 'high card', 2: 'one pair', 3: 'two pair',
   4: 'three of a kind', 5: 'straight', 6: 'flush',
   7: 'full house', 8: 'four of a kind', 9: 'straight flush',
   10: 'royal flush'
    }


class Pokergame:
    def __init__(self, player1: Pokerhand, player2: Pokerhand):
        self.player1 = player1
        self.player2 = player2

    def compare_hands(self):
        hand1, hand2 = self.player1.get_hand(), self.player2.get_hand()
        if self.player1 > self.player2:
            winner = ['player 1', HAND_VALUES[hand1]]
            loser = ['player 2', HAND_VALUES[hand2]]
        elif self.player1 < self.player2:
            winner = ['player 2', HAND_VALUES[hand2]]
            loser = ['player 1', HAND_VALUES[hand1]]
        else:
            winner = ['player 1', HAND_VALUES[hand1],
                      'player 2', HAND_VALUES[hand2]]
            loser = ['tie']
        return winner, loser


# ============================================================================
