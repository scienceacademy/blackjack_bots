class Bot:
    def __init__(self):
        self.seen = set()


    def blackjack_score(hand):
        score = 0
        aces = 0
        for card in hand:
            if card.rank >= 2 and card.rank <= 9:
                score = score + card.rank
            if card.rank >= 10:
                score = score + 10
            if card.rank == 1:
                aces = aces + 1
        for i in range(aces):
            if score + 11 <= 21:
                score = score + 11
            elif score + 1 > 21:
                score = score - 9
            else:
                score = score + 1
        return score
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand, blackjack_score):
        if blackjack_score(hand) == (10 or 11):
            return "double down"
        elif blackjack_score(hand) < 18:
            return "hit"
        else:
            return "stand"
