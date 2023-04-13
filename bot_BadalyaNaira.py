class Bot:
    def __init__(self):
        self.seen = set()

    def blackjack_score(self, hand):
        score = 0
        ace_number = 0
        for c in hand:
            if c.rank != 1:
                if c.rank >= 10:
                    score += 10
                else:
                    score += c.rank
        for c in hand:
            if c.rank == 1:
                ace_number += 1
        score = score + ace_number * 11
        while score > 21:
            score = score - 10
        return score

    def get_decision(self, dealer_up_card, hand, dealer_previous_hand):
        self.seen.add(dealer_up_card)
        for card in dealer_previous_hand:
            self.seen.add(card)
        for card in hand:
            self.seen.add(card)
        print(f"Dealer showing: {dealer_up_card}")
        print(f"Your hand: {hand}")
        print(f"Seen: {self.seen}")
        score = self.blackjack_score(hand)
        if score == 11:
            choice = "double down"
        elif score <= 17:
            choice = "hit"
        else:
            choice = "stand"
        return choice
