def blackjack_score(hand):
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

class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score = blackjack_score(hand)
        if score > 11:
            return "stand"
        elif score < 11:
            return "stand"
        elif score == 11:
            return "double down"
        elif score%2 == 0:
            return "split"
